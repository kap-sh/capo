from __future__ import annotations

from collections.abc import AsyncGenerator, AsyncIterator, Generator, Iterator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._body import Body, aclosing_bodies, closing_bodies
from capo_lambda._iter import ensure_async_iterator, ensure_sync_iterator
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.architectures_list
    import capo_lambda.types.blob
    import capo_lambda.types.blob_stream
    import capo_lambda.types.boolean
    import capo_lambda.types.capacity_provider_config
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.concurrency
    import capo_lambda.types.cors
    import capo_lambda.types.create_function_request
    import capo_lambda.types.create_function_url_config_request
    import capo_lambda.types.create_function_url_config_response
    import capo_lambda.types.dead_letter_config
    import capo_lambda.types.delete_function_code_signing_config_request
    import capo_lambda.types.delete_function_concurrency_request
    import capo_lambda.types.delete_function_url_config_request
    import capo_lambda.types.description
    import capo_lambda.types.durable_config
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.environment
    import capo_lambda.types.ephemeral_storage
    import capo_lambda.types.execution
    import capo_lambda.types.execution_status_list
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.file_system_config_list
    import capo_lambda.types.function_code
    import capo_lambda.types.function_configuration
    import capo_lambda.types.function_name
    import capo_lambda.types.function_scaling_config
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.function_url_function_name
    import capo_lambda.types.function_url_qualifier
    import capo_lambda.types.function_version
    import capo_lambda.types.function_version_latest_published
    import capo_lambda.types.get_function_code_signing_config_request
    import capo_lambda.types.get_function_code_signing_config_response
    import capo_lambda.types.get_function_concurrency_request
    import capo_lambda.types.get_function_concurrency_response
    import capo_lambda.types.get_function_configuration_request
    import capo_lambda.types.get_function_recursion_config_request
    import capo_lambda.types.get_function_recursion_config_response
    import capo_lambda.types.get_function_request
    import capo_lambda.types.get_function_response
    import capo_lambda.types.get_function_scaling_config_request
    import capo_lambda.types.get_function_scaling_config_response
    import capo_lambda.types.get_function_url_config_request
    import capo_lambda.types.get_function_url_config_response
    import capo_lambda.types.get_policy_request
    import capo_lambda.types.get_policy_response
    import capo_lambda.types.get_runtime_management_config_request
    import capo_lambda.types.get_runtime_management_config_response
    import capo_lambda.types.handler
    import capo_lambda.types.image_config
    import capo_lambda.types.invocation_request
    import capo_lambda.types.invocation_response
    import capo_lambda.types.invocation_type
    import capo_lambda.types.invoke_async_request
    import capo_lambda.types.invoke_async_response
    import capo_lambda.types.invoke_mode
    import capo_lambda.types.invoke_with_response_stream_request
    import capo_lambda.types.invoke_with_response_stream_response
    import capo_lambda.types.item_count
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.layer_list
    import capo_lambda.types.list_durable_executions_by_function_request
    import capo_lambda.types.list_durable_executions_by_function_response
    import capo_lambda.types.list_function_url_configs_request
    import capo_lambda.types.list_function_url_configs_response
    import capo_lambda.types.list_functions_request
    import capo_lambda.types.list_functions_response
    import capo_lambda.types.list_provisioned_concurrency_configs_request
    import capo_lambda.types.list_provisioned_concurrency_configs_response
    import capo_lambda.types.log_type
    import capo_lambda.types.logging_config
    import capo_lambda.types.master_region
    import capo_lambda.types.max_items
    import capo_lambda.types.max_list_items
    import capo_lambda.types.max_provisioned_concurrency_config_list_items
    import capo_lambda.types.memory_size
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.package_type
    import capo_lambda.types.published_function_qualifier
    import capo_lambda.types.put_function_code_signing_config_request
    import capo_lambda.types.put_function_code_signing_config_response
    import capo_lambda.types.put_function_concurrency_request
    import capo_lambda.types.put_function_recursion_config_request
    import capo_lambda.types.put_function_recursion_config_response
    import capo_lambda.types.put_function_scaling_config_request
    import capo_lambda.types.put_function_scaling_config_response
    import capo_lambda.types.put_runtime_management_config_request
    import capo_lambda.types.put_runtime_management_config_response
    import capo_lambda.types.recursive_loop
    import capo_lambda.types.reserved_concurrent_executions
    import capo_lambda.types.response_streaming_invocation_type
    import capo_lambda.types.reverse_order
    import capo_lambda.types.role_arn
    import capo_lambda.types.runtime
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.s3_bucket
    import capo_lambda.types.s3_key
    import capo_lambda.types.s3_object_storage_mode
    import capo_lambda.types.s3_object_version
    import capo_lambda.types.snap_start
    import capo_lambda.types.string
    import capo_lambda.types.tags
    import capo_lambda.types.tenancy_config
    import capo_lambda.types.tenant_id
    import capo_lambda.types.timeout
    import capo_lambda.types.tracing_config
    import capo_lambda.types.unqualified_function_name
    import capo_lambda.types.update_function_code_request
    import capo_lambda.types.update_function_configuration_request
    import capo_lambda.types.update_function_url_config_request
    import capo_lambda.types.update_function_url_config_response
    import capo_lambda.types.update_runtime_on
    import capo_lambda.types.vpc_config
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class Function:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        role: "capo_lambda.types.role_arn.RoleArn",
        code: "capo_lambda.types.function_code.FunctionCode",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        package_type: Optional["capo_lambda.types.package_type.PackageType"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        code_signing_config_arn: Optional[
            "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        tenancy_config: Optional[
            "capo_lambda.types.tenancy_config.TenancyConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Creates a Lambda function. To create a function, you need a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html\">deployment package</a> and an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role\">execution role</a>. The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use Amazon Web Services services, such as Amazon CloudWatch Logs for log streaming and X-Ray for request tracing.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a>, then you set the package type to <code>Image</code>. For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>, then you set the package type to <code>Zip</code>. For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>). If you do not specify the architecture, then the default value is <code>x86-64</code>.</p> <p>When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can't invoke or modify the function. The <code>State</code>, <code>StateReason</code>, and <code>StateReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the function is ready to invoke. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the <code>Publish</code> parameter to create version <code>1</code> of your function from its initial configuration.</p> <p>The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with <a>UpdateFunctionConfiguration</a>. Function-level settings apply to both the unpublished and published versions of the function, and include tags (<a>TagResource</a>) and per-function concurrency limits (<a>PutFunctionConcurrency</a>).</p> <p>You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with <a>UpdateFunctionCode</a>, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes set of signing profiles, which define the trusted publishers for this function.</p> <p>If another Amazon Web Services account or an Amazon Web Services service invokes your function, use <a>AddPermission</a> to grant permission by creating a resource-based Identity and Access Management (IAM) policy. You can grant permissions at the function level, on a version, or on an alias.</p> <p>To invoke your function directly, use <a>Invoke</a>. To invoke your function in response to events in other Amazon Web Services services, create an event source mapping (<a>CreateEventSourceMapping</a>), or configure a function trigger in the other service. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html\">Invoking Lambda functions</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            code: <p>The code for the function.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            publish: <p>Set to true to publish the first version of the function during creation.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            package_type: <p>The type of deployment package. Set to <code>Image</code> for container image and set to <code>Zip</code> for .zip file archive.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            tags: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to apply to the function.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            code_signing_config_arn: <p>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</p>
            image_config: <p>Container image <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">configuration values</a> that override the values in the container image Dockerfile.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            tenancy_config: <p>Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource allocations. Required for functions supporting multiple tenants.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for durable functions. Enables creating functions with durability that can remember their state and continue execution even after interruptions.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a function
            The following example creates a function with a deployment package in Amazon S3 and enables X-Ray tracing and environment variable encryption.

            >>> client.put(code={'S3Bucket': 'my-bucket-1xpuxmplzrlbh', 'S3Key': 'function.zip'}, description='Process image objects from Amazon S3.', durable_config={'ExecutionTimeout': 31622400, 'RetentionPeriodInDays': 30}, environment={'Variables': {'BUCKET': 'my-bucket-1xpuxmplzrlbh', 'PREFIX': 'inbound'}}, function_name='my-function', handler='index.handler', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966', memory_size=256, publish=True, role='arn:aws:iam::123456789012:role/lambda-role', runtime='nodejs12.x', tags={'DEPARTMENT': 'Assets'}, timeout=15, tracing_config={'Mode': 'Active'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_function_request.CreateFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_function.create_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_request.CreateFunctionRequest = {
            "function_name": function_name,
            "role": role,
            "code": code,
        }
        if runtime is not None:
            input_["runtime"] = runtime
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if package_type is not None:
            input_["package_type"] = package_type
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if tags is not None:
            input_["tags"] = tags
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if code_signing_config_arn is not None:
            input_["code_signing_config_arn"] = code_signing_config_arn
        if image_config is not None:
            input_["image_config"] = image_config
        if architectures is not None:
            input_["architectures"] = architectures
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if tenancy_config is not None:
            input_["tenancy_config"] = tenancy_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        master_region: Optional["capo_lambda.types.master_region.MasterRegion"] = None,
        function_version: Optional[
            "capo_lambda.types.function_version.FunctionVersion"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_response.ListFunctionsResponse":
        """<p>Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.</p> <p>Set <code>FunctionVersion</code> to <code>ALL</code> to include all published versions of each function in addition to the unpublished version.</p> <note> <p>The <code>ListFunctions</code> operation returns a subset of the <a>FunctionConfiguration</a> fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use <a>GetFunction</a>.</p> </note>

        Args:
            master_region: <p>For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, <code>us-east-1</code> filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set <code>FunctionVersion</code> to <code>ALL</code>.</p>
            function_version: <p>Set to <code>ALL</code> to include entries for all published versions of each function.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of functions to return in the response. Note that <code>ListFunctions</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of Lambda functions
            This operation returns a list of Lambda functions.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_request.ListFunctionsRequest = {}
        if master_region is not None:
            input_["master_region"] = master_region
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes a concurrent execution limit from a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove the reserved concurrent execution limit from a function
            The following example deletes the reserved concurrent execution limit from a function named my-function.

            >>> client.delete_function_concurrency(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_concurrency.delete_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse":
        r"""<p>Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use <a>PutFunctionConcurrency</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the reserved concurrency setting for a function
            The following example returns the reserved concurrency setting for a function named my-function.

            >>> client.get_function_concurrency(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_concurrency.get_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_provisioned_concurrency_configs(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_provisioned_concurrency_config_list_items.MaxProvisionedConcurrencyConfigListItems"
        ] = None,
    ) -> "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse":
        r"""<p>Retrieves a list of provisioned concurrency configurations for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Specify a number to limit the number of configurations returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of provisioned concurrency configurations
            The following example returns a list of provisioned concurrency configurations for a function named my-function.

            >>> client.list_provisioned_concurrency_configs(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs.list_provisioned_concurrency_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        reserved_concurrent_executions: "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.concurrency.Concurrency":
        r"""<p>Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level.</p> <p>Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use <a>GetFunction</a> to see the current setting for a function.</p> <p>Use <a>GetAccountSettings</a> to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html\">Lambda function scaling</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            reserved_concurrent_executions: <p>The number of simultaneous executions to reserve for the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure a reserved concurrency limit for a function
            The following example configures 100 reserved concurrent executions for the my-function function.

            >>> client.put_function_concurrency(function_name='my-function', reserved_concurrent_executions=100)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest]",
        ) -> OperationResponse["capo_lambda.types.concurrency.Concurrency"]:
            import capo_lambda._operations.aws_gir_api_service.put_function_concurrency

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_concurrency.put_function_concurrency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest = {
            "function_name": function_name,
            "reserved_concurrent_executions": reserved_concurrent_executions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_code(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        zip_file: Optional["capo_lambda.types.blob.Blob"] = None,
        s3_bucket: Optional["capo_lambda.types.s3_bucket.S3Bucket"] = None,
        s3_key: Optional["capo_lambda.types.s3_key.S3Key"] = None,
        s3_object_version: Optional[
            "capo_lambda.types.s3_object_version.S3ObjectVersion"
        ] = None,
        s3_object_storage_mode: Optional[
            "capo_lambda.types.s3_object_storage_mode.S3ObjectStorageMode"
        ] = None,
        image_uri: Optional["capo_lambda.types.string.String"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        dry_run: Optional["capo_lambda.types.boolean.Boolean"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        source_kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html\">Configuring code signing for Lambda</a>.</p> <p>If the function's package type is <code>Image</code>, then you must specify the code package in <code>ImageUri</code> as the URI of a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a> in the Amazon ECR registry.</p> <p>If the function's package type is <code>Zip</code>, then you must specify the deployment package as a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>. Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the <code>ZipFile</code> field.</p> <p>The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>).</p> <p>The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version.</p> <note> <p>For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            zip_file: <p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_bucket: <p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_key: <p>The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_object_version: <p>For versioned objects, the version of the deployment package object to use.</p>
            s3_object_storage_mode: <p>Specifies how the deployment package is stored. Valid values:</p> <ul> <li> <p> <code>COPY</code> (default) – Uploads a copy of your deployment package to Lambda.</p> </li> <li> <p> <code>REFERENCE</code> – Lambda references the deployment package from the specified Amazon S3 bucket.</p> </li> </ul>
            image_uri: <p>URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            publish: <p>Set to true to publish a new version of the function after updating the code. This has the same effect as calling <a>PublishVersion</a> separately.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            dry_run: <p>Set to true to validate the request parameters and access permissions without modifying the function code.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            source_kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an Amazon Web Services managed key.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's code
            The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.

            >>> client.update_function_code(function_name='my-function', s3_bucket='my-bucket-1xpuxmplzrlbh', s3_key='function.zip')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_code

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_code.update_function_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest = {
            "function_name": function_name
        }
        if zip_file is not None:
            input_["zip_file"] = zip_file
        if s3_bucket is not None:
            input_["s3_bucket"] = s3_bucket
        if s3_key is not None:
            input_["s3_key"] = s3_key
        if s3_object_version is not None:
            input_["s3_object_version"] = s3_object_version
        if s3_object_storage_mode is not None:
            input_["s3_object_storage_mode"] = s3_object_storage_mode
        if image_uri is not None:
            input_["image_uri"] = image_uri
        if architectures is not None:
            input_["architectures"] = architectures
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if source_kms_key_arn is not None:
            input_["source_kms_key_arn"] = source_kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_configuration(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        role: Optional["capo_lambda.types.role_arn.RoleArn"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Modify the version-specific settings of a Lambda function.</p> <p>When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can't modify the function, but you can still invoke it. The <code>LastUpdateStatus</code>, <code>LastUpdateStatusReason</code>, and <code>LastUpdateStatusReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the update is complete and the function is processing events with the new configuration. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>These settings can vary between versions of a function and are locked when you publish a version. You can't modify the configuration of a published version, only the unpublished version.</p> <p>To configure function concurrency, use <a>PutFunctionConcurrency</a>. To grant invoke permissions to an Amazon Web Services account or Amazon Web Services service, use <a>AddPermission</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            image_config: <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">Container image configuration values</a> that override the values in the container image Docker file.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable functions</a>, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's configuration
            The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.

            >>> client.update_function_configuration(durable_config={'ExecutionTimeout': 3600, 'RetentionPeriodInDays': 45}, function_name='my-function', memory_size=256)
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_configuration

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_configuration.update_function_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if role is not None:
            input_["role"] = role
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if environment is not None:
            input_["environment"] = environment
        if runtime is not None:
            input_["runtime"] = runtime
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if image_config is not None:
            input_["image_config"] = image_config
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        auth_type: "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse":
        r"""<p>Creates a Lambda function URL with the specified configuration parameters. A function URL is a dedicated HTTP(S) endpoint that you can use to invoke your function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_function_url_config.create_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest = {
            "function_name": function_name,
            "auth_type": auth_type,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes the code signing configuration from the function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config.delete_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes a Lambda function URL. When you delete a function URL, you can't recover it. Creating a new function URL results in a different URL address.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_function_url_config.delete_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_response.GetFunctionResponse":
        r"""<p>Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function
            The following example returns code and configuration details for version 1 of a function named my-function.

            >>> client.get_function(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_request.GetFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse":
        r"""<p>Returns the code signing configuration for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config.get_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_configuration(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use <a>UpdateFunctionConfiguration</a>.</p> <p>To get all of a function's details, including function-level settings, use <a>GetFunction</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns and configuration details for version 1 of a function named my-function.

            >>> client.get_function_configuration(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_configuration

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_configuration.get_function_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse":
        r"""<p>Returns your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration. </p>

        Args:
            function_name: <p>The name of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_recursion_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_recursion_config.get_function_recursion_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest = {
            "function_name": function_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse":
        """<p>Retrieves the scaling configuration for a Lambda Managed Instances function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to get the scaling configuration for a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_scaling_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_scaling_config.get_function_scaling_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse":
        r"""<p>Returns details about a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_function_url_config.get_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_policy_response.GetPolicyResponse":
        r"""<p>Returns the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html\">resource-based IAM policy</a> for a function, version, or alias.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get the policy for that resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve a Lambda function policy
            The following example returns the resource-based policy for version 1 of a Lambda function named my-function.

            >>> client.get_policy(function_name='my-function', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_policy

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_policy_request.GetPolicyRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse":
        r"""<p>Retrieves the runtime management configuration for a function's version. If the runtime update mode is <b>Manual</b>, this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is <b>Auto</b> or <b>Function update</b>, this includes the runtime update mode and <code>null</code> is returned for the ARN. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_runtime_management_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_runtime_management_config.get_runtime_management_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        invocation_type: Optional[
            "capo_lambda.types.invocation_type.InvocationType"
        ] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
    ) -> "capo_lambda.types.invocation_response.InvocationResponse":
        r"""<p>Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the<code>InvocationType</code> is <code>RequestResponse</code>). To invoke a function asynchronously, set <code>InvocationType</code> to <code>Event</code>. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p> <p>For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html\">synchronous invocation</a>, details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html\">execution log</a> and <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html\">trace</a>.</p> <p>When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html\">Error handling and automatic retries in Lambda</a>.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a>, Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">dead-letter queue</a>.</p> <p>The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">quota</a> errors, or issues with your function's code and configuration. For example, Lambda returns <code>TooManyRequestsException</code> if running the function would cause you to exceed a concurrency limit at either the account level (<code>ConcurrentInvocationLimitExceeded</code>) or function level (<code>ReservedFunctionConcurrentInvocationLimitExceeded</code>).</p> <p>For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invocation_type: <p>Choose from the following options.</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.</p> </li> <li> <p> <code>Event</code> – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the user or role has permission to invoke the function.</p> </li> </ul>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p>
            durable_execution_name: <p>A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a <code>DurableExecutionAlreadyStartedException</code> error.</p> <p>If not specified, Lambda generates a unique identifier automatically. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names\">Execution names</a>.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            qualifier: <p>Specify a version or alias to invoke a published version of the function.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>

        Raises:
            capo_lambda.errors.code_artifact_user_deleted_exception.CodeArtifactUserDeletedException: <p>The Lambda function couldn't be invoked because its code artifact user has been deleted. Wait for Lambda to provision a new code artifact user, or update the function's code package to recreate it.</p>
            capo_lambda.errors.code_artifact_user_failed_exception.CodeArtifactUserFailedException: <p>The Lambda function couldn't be invoked because provisioning of its code artifact user failed. Update the function's code package or check the Lambda function's <code>State</code> and <code>StateReasonCode</code> for additional context.</p>
            capo_lambda.errors.code_artifact_user_pending_exception.CodeArtifactUserPendingException: <p>The Lambda function couldn't be invoked because its code artifact user is still being provisioned. Wait for the function's <code>State</code> to become <code>Active</code> and try the request again.</p>
            capo_lambda.errors.durable_execution_already_started_exception.DurableExecutionAlreadyStartedException: <p>The durable execution with the specified name has already been started. Each durable execution name must be unique within the function. Use a different name or check the status of the existing execution.</p>
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.eni_not_ready_exception.ENINotReadyException: <p>Lambda couldn't invoke the Lambda function because the elastic network interface (ENI) configured for its VPC connection isn't ready yet. Wait a few moments and try the request again. For more information about VPC configuration, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function
            The following example invokes version 1 of a function named my-function with an empty event payload.

            >>> client.invoke(durable_execution_name='myExecution', function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
            To invoke a Lambda function asynchronously
            The following example invokes version 1 of a function named my-function asynchronously.

            >>> client.invoke(function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invocation_request.InvocationRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invocation_response.InvocationResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke.invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invocation_request.InvocationRequest = {
            "function_name": function_name
        }
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if payload is not None:
            input_["payload"] = payload
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_async(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        invoke_args: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.invoke_async_response.InvokeAsyncResponse":
        r"""<note> <p>For asynchronous function invocation, use <a>Invoke</a>.</p> </note> <p>Invokes a function asynchronously.</p> <note> <p>The payload limit is 256KB. For larger payloads, for up to 1MB, use <a>Invoke</a>.</p> </note> <note> <p>If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invoke_args: <p>The JSON that you want to provide to your Lambda function as input.</p>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function asynchronously
            The following example invokes a Lambda function asynchronously

            >>> client.invoke_async(function_name='my-function', invoke_args='{}')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invoke_async_request.InvokeAsyncRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invoke_async_response.InvokeAsyncResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_async

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke_async.invoke_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest = {
            "function_name": function_name,
            "invoke_args": ensure_sync_iterator(invoke_args),
        }

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output

    @contextmanager
    def invoke_with_response_stream(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
        invocation_type: Optional[
            "capo_lambda.types.response_streaming_invocation_type.ResponseStreamingInvocationType"
        ] = None,
    ) -> "Generator[capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse]":
        r"""<p>Configure your Lambda functions to stream response payloads back to clients. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html\">Configuring a Lambda function to stream responses</a>.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.</p>
            qualifier: <p>The alias name.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>
            invocation_type: <p>Use one of the following options:</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the IAM user or role has permission to invoke the function.</p> </li> </ul>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream.invoke_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest = {
            "function_name": function_name
        }
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if payload is not None:
            input_["payload"] = payload
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_durable_executions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "capo_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable executions</a> for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>
            qualifier: <p>The function version or alias. If not specified, lists executions for the $LATEST version.</p>
            durable_execution_name: <p>Filter executions by name. Only executions with names that matches this string are returned.</p>
            statuses: <p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>
            started_after: <p>Filter executions that started after this timestamp (ISO 8601 format).</p>
            started_before: <p>Filter executions that started before this timestamp (ISO 8601 format).</p>
            reverse_order: <p>Set to true to return results in chronological order (oldest first). Default is false.</p>
            marker: <p>Pagination token from a previous request to continue retrieving results.</p>
            max_items: <p>Maximum number of executions to return (1-1000). Default is 100.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function.list_durable_executions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if statuses is not None:
            input_["statuses"] = statuses
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_function_url_configs(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_items.MaxItems"] = None,
    ) -> "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse":
        r"""<p>Returns a list of Lambda function URLs for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function URLs to return in the response. Note that <code>ListFunctionUrlConfigs</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_url_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_function_url_configs.list_function_url_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse":
        r"""<p>Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config.put_function_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn,
            "function_name": function_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        recursive_loop: "capo_lambda.types.recursive_loop.RecursiveLoop",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse":
        r"""<p>Sets your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration.</p> <p>When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.</p> <p>Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to <code>Terminate</code>, it stops your function being invoked and notifies you.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            recursive_loop: <p>If you set your function's recursive loop detection configuration to <code>Allow</code>, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes it.</p> <p>If you set your function's recursive loop detection configuration to <code>Terminate</code>, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.</p> <p>By default, Lambda sets your function's configuration to <code>Terminate</code>.</p> <important> <p>If your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your Amazon Web Services account. To learn more about best practices for using recursive invocation patterns, see <a href=\"https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway\">Recursive patterns that cause run-away Lambda functions</a> in Serverless Land.</p> </important>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_recursion_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_recursion_config.put_function_recursion_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest = {
            "function_name": function_name,
            "recursive_loop": recursive_loop,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_scaling_config: Optional[
            "capo_lambda.types.function_scaling_config.FunctionScalingConfig"
        ] = None,
    ) -> "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse":
        """<p>Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to set the scaling configuration for a published version of the function.</p>
            function_scaling_config: <p>The scaling configuration to apply to the function, including minimum and maximum execution environment limits.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_scaling_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_function_scaling_config.put_function_scaling_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }
        if function_scaling_config is not None:
            input_["function_scaling_config"] = function_scaling_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        update_runtime_on: "capo_lambda.types.update_runtime_on.UpdateRuntimeOn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        runtime_version_arn: Optional[
            "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
        ] = None,
    ) -> "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse":
        r"""<p>Sets the runtime management configuration for a function's version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>
            update_runtime_on: <p>Specify the runtime update mode.</p> <ul> <li> <p> <b>Auto (default)</b> - Automatically update to the most recent and secure runtime version using a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase\">Two-phase runtime version rollout</a>. This is the best choice for most customers to ensure they always benefit from runtime updates.</p> </li> <li> <p> <b>Function update</b> - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.</p> </li> <li> <p> <b>Manual</b> - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback\">Roll back a runtime version</a>.</p> </li> </ul>
            runtime_version_arn: <p>The ARN of the runtime version you want the function to use.</p> <note> <p>This is only required if you're using the <b>Manual</b> runtime update mode.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_runtime_management_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_runtime_management_config.put_runtime_management_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest = {
            "function_name": function_name,
            "update_runtime_on": update_runtime_on,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if runtime_version_arn is not None:
            input_["runtime_version_arn"] = runtime_version_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse":
        r"""<p>Updates the configuration for a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_url_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_function_url_config.update_function_url_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFunction:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        role: "capo_lambda.types.role_arn.RoleArn",
        code: "capo_lambda.types.function_code.FunctionCode",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        package_type: Optional["capo_lambda.types.package_type.PackageType"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        code_signing_config_arn: Optional[
            "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        tenancy_config: Optional[
            "capo_lambda.types.tenancy_config.TenancyConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Creates a Lambda function. To create a function, you need a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html\">deployment package</a> and an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role\">execution role</a>. The deployment package is a .zip file archive or container image that contains your function code. The execution role grants the function permission to use Amazon Web Services services, such as Amazon CloudWatch Logs for log streaming and X-Ray for request tracing.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a>, then you set the package type to <code>Image</code>. For a container image, the code property must include the URI of a container image in the Amazon ECR registry. You do not need to specify the handler and runtime properties.</p> <p>If the deployment package is a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>, then you set the package type to <code>Zip</code>. For a .zip file archive, the code property specifies the location of the .zip file. You must also specify the handler and runtime properties. The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>). If you do not specify the architecture, then the default value is <code>x86-64</code>.</p> <p>When you create a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute or so. During this time, you can't invoke or modify the function. The <code>State</code>, <code>StateReason</code>, and <code>StateReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the function is ready to invoke. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>A function has an unpublished version, and can have published versions and aliases. The unpublished version changes when you update your function's code and configuration. A published version is a snapshot of your function code and configuration that can't be changed. An alias is a named resource that maps to a version, and can be changed to map to a different version. Use the <code>Publish</code> parameter to create version <code>1</code> of your function from its initial configuration.</p> <p>The other parameters let you configure version-specific and function-level settings. You can modify version-specific settings later with <a>UpdateFunctionConfiguration</a>. Function-level settings apply to both the unpublished and published versions of the function, and include tags (<a>TagResource</a>) and per-function concurrency limits (<a>PutFunctionConcurrency</a>).</p> <p>You can use code signing if your deployment package is a .zip file archive. To enable code signing for this function, specify the ARN of a code-signing configuration. When a user attempts to deploy a code package with <a>UpdateFunctionCode</a>, Lambda checks that the code package has a valid signature from a trusted publisher. The code-signing configuration includes set of signing profiles, which define the trusted publishers for this function.</p> <p>If another Amazon Web Services account or an Amazon Web Services service invokes your function, use <a>AddPermission</a> to grant permission by creating a resource-based Identity and Access Management (IAM) policy. You can grant permissions at the function level, on a version, or on an alias.</p> <p>To invoke your function directly, use <a>Invoke</a>. To invoke your function in response to events in other Amazon Web Services services, create an event source mapping (<a>CreateEventSourceMapping</a>), or configure a function trigger in the other service. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html\">Invoking Lambda functions</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            code: <p>The code for the function.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            publish: <p>Set to true to publish the first version of the function during creation.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            package_type: <p>The type of deployment package. Set to <code>Image</code> for container image and set to <code>Zip</code> for .zip file archive.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            tags: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to apply to the function.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            code_signing_config_arn: <p>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</p>
            image_config: <p>Container image <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">configuration values</a> that override the values in the container image Dockerfile.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            tenancy_config: <p>Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource allocations. Required for functions supporting multiple tenants.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for durable functions. Enables creating functions with durability that can remember their state and continue execution even after interruptions.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a function
            The following example creates a function with a deployment package in Amazon S3 and enables X-Ray tracing and environment variable encryption.

            >>> await client.put(code={'S3Bucket': 'my-bucket-1xpuxmplzrlbh', 'S3Key': 'function.zip'}, description='Process image objects from Amazon S3.', durable_config={'ExecutionTimeout': 31622400, 'RetentionPeriodInDays': 30}, environment={'Variables': {'BUCKET': 'my-bucket-1xpuxmplzrlbh', 'PREFIX': 'inbound'}}, function_name='my-function', handler='index.handler', kms_key_arn='arn:aws:kms:us-west-2:123456789012:key/b0844d6c-xmpl-4463-97a4-d49f50839966', memory_size=256, publish=True, role='arn:aws:iam::123456789012:role/lambda-role', runtime='nodejs12.x', tags={'DEPARTMENT': 'Assets'}, timeout=15, tracing_config={'Mode': 'Active'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_function_request.CreateFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_function.async_create_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_request.CreateFunctionRequest = {
            "function_name": function_name,
            "role": role,
            "code": code,
        }
        if runtime is not None:
            input_["runtime"] = runtime
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if package_type is not None:
            input_["package_type"] = package_type
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if tags is not None:
            input_["tags"] = tags
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if code_signing_config_arn is not None:
            input_["code_signing_config_arn"] = code_signing_config_arn
        if image_config is not None:
            input_["image_config"] = image_config
        if architectures is not None:
            input_["architectures"] = architectures
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if tenancy_config is not None:
            input_["tenancy_config"] = tenancy_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        master_region: Optional["capo_lambda.types.master_region.MasterRegion"] = None,
        function_version: Optional[
            "capo_lambda.types.function_version.FunctionVersion"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_response.ListFunctionsResponse":
        """<p>Returns a list of Lambda functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.</p> <p>Set <code>FunctionVersion</code> to <code>ALL</code> to include all published versions of each function in addition to the unpublished version.</p> <note> <p>The <code>ListFunctions</code> operation returns a subset of the <a>FunctionConfiguration</a> fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use <a>GetFunction</a>.</p> </note>

        Args:
            master_region: <p>For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, <code>us-east-1</code> filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set <code>FunctionVersion</code> to <code>ALL</code>.</p>
            function_version: <p>Set to <code>ALL</code> to include entries for all published versions of each function.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of functions to return in the response. Note that <code>ListFunctions</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of Lambda functions
            This operation returns a list of Lambda functions.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_functions_request.ListFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_functions.async_list_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_request.ListFunctionsRequest = {}
        if master_region is not None:
            input_["master_region"] = master_region
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes a concurrent execution limit from a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove the reserved concurrent execution limit from a function
            The following example deletes the reserved concurrent execution limit from a function named my-function.

            >>> await client.delete_function_concurrency(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_concurrency

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_function_concurrency.async_delete_function_concurrency(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_concurrency_request.DeleteFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse":
        r"""<p>Returns details about the reserved concurrency configuration for a function. To set a concurrency limit for a function, use <a>PutFunctionConcurrency</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the reserved concurrency setting for a function
            The following example returns the reserved concurrency setting for a function named my-function.

            >>> await client.get_function_concurrency(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_concurrency_response.GetFunctionConcurrencyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_concurrency

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_concurrency.async_get_function_concurrency(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_concurrency_request.GetFunctionConcurrencyRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_provisioned_concurrency_configs(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional[
            "capo_lambda.types.max_provisioned_concurrency_config_list_items.MaxProvisionedConcurrencyConfigListItems"
        ] = None,
    ) -> "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse":
        r"""<p>Retrieves a list of provisioned concurrency configurations for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Specify a number to limit the number of configurations returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of provisioned concurrency configurations
            The following example returns a list of provisioned concurrency configurations for a function named my-function.

            >>> await client.list_provisioned_concurrency_configs(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_provisioned_concurrency_configs_response.ListProvisionedConcurrencyConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_provisioned_concurrency_configs.async_list_provisioned_concurrency_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_provisioned_concurrency_configs_request.ListProvisionedConcurrencyConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_function_concurrency(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        reserved_concurrent_executions: "capo_lambda.types.reserved_concurrent_executions.ReservedConcurrentExecutions",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.concurrency.Concurrency":
        r"""<p>Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level.</p> <p>Concurrency settings apply to the function as a whole, including all published versions and the unpublished version. Reserving concurrency both ensures that your function has capacity to process the specified number of events simultaneously, and prevents it from scaling beyond that level. Use <a>GetFunction</a> to see the current setting for a function.</p> <p>Use <a>GetAccountSettings</a> to see your Regional concurrency limit. You can reserve concurrency for as many functions as you like, as long as you leave at least 100 simultaneous executions unreserved for functions that aren't configured with a per-function limit. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html\">Lambda function scaling</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            reserved_concurrent_executions: <p>The number of simultaneous executions to reserve for the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure a reserved concurrency limit for a function
            The following example configures 100 reserved concurrent executions for the my-function function.

            >>> await client.put_function_concurrency(function_name='my-function', reserved_concurrent_executions=100)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest]",
        ) -> AsyncOperationResponse["capo_lambda.types.concurrency.Concurrency"]:
            import capo_lambda._operations.aws_gir_api_service.put_function_concurrency

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_function_concurrency.async_put_function_concurrency(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_concurrency_request.PutFunctionConcurrencyRequest = {
            "function_name": function_name,
            "reserved_concurrent_executions": reserved_concurrent_executions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_function_code(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        zip_file: Optional["capo_lambda.types.blob.Blob"] = None,
        s3_bucket: Optional["capo_lambda.types.s3_bucket.S3Bucket"] = None,
        s3_key: Optional["capo_lambda.types.s3_key.S3Key"] = None,
        s3_object_version: Optional[
            "capo_lambda.types.s3_object_version.S3ObjectVersion"
        ] = None,
        s3_object_storage_mode: Optional[
            "capo_lambda.types.s3_object_storage_mode.S3ObjectStorageMode"
        ] = None,
        image_uri: Optional["capo_lambda.types.string.String"] = None,
        architectures: Optional[
            "capo_lambda.types.architectures_list.ArchitecturesList"
        ] = None,
        publish: Optional["capo_lambda.types.boolean.Boolean"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
        dry_run: Optional["capo_lambda.types.boolean.Boolean"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        source_kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Updates a Lambda function's code. If code signing is enabled for the function, the code package must be signed by a trusted publisher. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html\">Configuring code signing for Lambda</a>.</p> <p>If the function's package type is <code>Image</code>, then you must specify the code package in <code>ImageUri</code> as the URI of a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html\">container image</a> in the Amazon ECR registry.</p> <p>If the function's package type is <code>Zip</code>, then you must specify the deployment package as a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html#gettingstarted-package-zip\">.zip file archive</a>. Enter the Amazon S3 bucket and key of the code .zip file location. You can also provide the function code inline using the <code>ZipFile</code> field.</p> <p>The code in the deployment package must be compatible with the target instruction set architecture of the function (<code>x86-64</code> or <code>arm64</code>).</p> <p>The function's code is locked when you publish a version. You can't modify the code of a published version, only the unpublished version.</p> <note> <p>For a function defined as a container image, Lambda resolves the image tag to an image digest. In Amazon ECR, if you update the image tag to a new image, Lambda does not automatically update the function.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            zip_file: <p>The base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for you. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_bucket: <p>An Amazon S3 bucket in the same Amazon Web Services Region as your function. The bucket can be in a different Amazon Web Services account. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_key: <p>The Amazon S3 key of the deployment package. Use only with a function defined with a .zip file archive deployment package.</p>
            s3_object_version: <p>For versioned objects, the version of the deployment package object to use.</p>
            s3_object_storage_mode: <p>Specifies how the deployment package is stored. Valid values:</p> <ul> <li> <p> <code>COPY</code> (default) – Uploads a copy of your deployment package to Lambda.</p> </li> <li> <p> <code>REFERENCE</code> – Lambda references the deployment package from the specified Amazon S3 bucket.</p> </li> </ul>
            image_uri: <p>URI of a container image in the Amazon ECR registry. Do not use for a function defined with a .zip file archive.</p>
            architectures: <p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>
            publish: <p>Set to true to publish a new version of the function after updating the code. This has the same effect as calling <a>PublishVersion</a> separately.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>
            dry_run: <p>Set to true to validate the request parameters and access permissions without modifying the function code.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            source_kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an Amazon Web Services managed key.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's code
            The following example replaces the code of the unpublished ($LATEST) version of a function named my-function with the contents of the specified zip file in Amazon S3.

            >>> await client.update_function_code(function_name='my-function', s3_bucket='my-bucket-1xpuxmplzrlbh', s3_key='function.zip')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_code

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_function_code.async_update_function_code(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_code_request.UpdateFunctionCodeRequest = {
            "function_name": function_name
        }
        if zip_file is not None:
            input_["zip_file"] = zip_file
        if s3_bucket is not None:
            input_["s3_bucket"] = s3_bucket
        if s3_key is not None:
            input_["s3_key"] = s3_key
        if s3_object_version is not None:
            input_["s3_object_version"] = s3_object_version
        if s3_object_storage_mode is not None:
            input_["s3_object_storage_mode"] = s3_object_storage_mode
        if image_uri is not None:
            input_["image_uri"] = image_uri
        if architectures is not None:
            input_["architectures"] = architectures
        if publish is not None:
            input_["publish"] = publish
        if publish_to is not None:
            input_["publish_to"] = publish_to
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if source_kms_key_arn is not None:
            input_["source_kms_key_arn"] = source_kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_function_configuration(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        role: Optional["capo_lambda.types.role_arn.RoleArn"] = None,
        handler: Optional["capo_lambda.types.handler.Handler"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        timeout: Optional["capo_lambda.types.timeout.Timeout"] = None,
        memory_size: Optional["capo_lambda.types.memory_size.MemorySize"] = None,
        vpc_config: Optional["capo_lambda.types.vpc_config.VpcConfig"] = None,
        environment: Optional["capo_lambda.types.environment.Environment"] = None,
        runtime: Optional["capo_lambda.types.runtime.Runtime"] = None,
        dead_letter_config: Optional[
            "capo_lambda.types.dead_letter_config.DeadLetterConfig"
        ] = None,
        kms_key_arn: Optional["capo_lambda.types.kms_key_arn.KMSKeyArn"] = None,
        tracing_config: Optional[
            "capo_lambda.types.tracing_config.TracingConfig"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        layers: Optional["capo_lambda.types.layer_list.LayerList"] = None,
        file_system_configs: Optional[
            "capo_lambda.types.file_system_config_list.FileSystemConfigList"
        ] = None,
        image_config: Optional["capo_lambda.types.image_config.ImageConfig"] = None,
        ephemeral_storage: Optional[
            "capo_lambda.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        snap_start: Optional["capo_lambda.types.snap_start.SnapStart"] = None,
        logging_config: Optional[
            "capo_lambda.types.logging_config.LoggingConfig"
        ] = None,
        capacity_provider_config: Optional[
            "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
        ] = None,
        durable_config: Optional[
            "capo_lambda.types.durable_config.DurableConfig"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Modify the version-specific settings of a Lambda function.</p> <p>When you update a function, Lambda provisions an instance of the function and its supporting resources. If your function connects to a VPC, this process can take a minute. During this time, you can't modify the function, but you can still invoke it. The <code>LastUpdateStatus</code>, <code>LastUpdateStatusReason</code>, and <code>LastUpdateStatusReasonCode</code> fields in the response from <a>GetFunctionConfiguration</a> indicate when the update is complete and the function is processing events with the new configuration. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">Lambda function states</a>.</p> <p>These settings can vary between versions of a function and are locked when you publish a version. You can't modify the configuration of a published version, only the unpublished version.</p> <p>To configure function concurrency, use <a>PutFunctionConcurrency</a>. To grant invoke permissions to an Amazon Web Services account or Amazon Web Services service, use <a>AddPermission</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            role: <p>The Amazon Resource Name (ARN) of the function's execution role.</p>
            handler: <p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>
            description: <p>A description of the function.</p>
            timeout: <p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>
            memory_size: <p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>
            vpc_config: <p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            environment: <p>Environment variables that are accessible from function code during execution.</p>
            runtime: <p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>
            dead_letter_config: <p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>
            kms_key_arn: <p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>
            tracing_config: <p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>
            revision_id: <p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>
            layers: <p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>
            file_system_configs: <p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>
            image_config: <p> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">Container image configuration values</a> that override the values in the container image Docker file.</p>
            ephemeral_storage: <p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>
            snap_start: <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>
            logging_config: <p>The function's Amazon CloudWatch Logs configuration settings.</p>
            capacity_provider_config: <p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>
            durable_config: <p>Configuration settings for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable functions</a>, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.code_verification_failed_exception.CodeVerificationFailedException: <p>The code signature failed one or more of the validation checks for signature mismatch or expiry, and the code signing policy is set to ENFORCE. Lambda blocks the deployment.</p>
            capo_lambda.errors.invalid_code_signature_exception.InvalidCodeSignatureException: <p>The code signature failed the integrity check. If the integrity check fails, then Lambda blocks deployment, even if the code signing policy is set to WARN.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a Lambda function's configuration
            The following example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of a function named my-function.

            >>> await client.update_function_configuration(durable_config={'ExecutionTimeout': 3600, 'RetentionPeriodInDays': 45}, function_name='my-function', memory_size=256)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_configuration

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_function_configuration.async_update_function_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_configuration_request.UpdateFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if role is not None:
            input_["role"] = role
        if handler is not None:
            input_["handler"] = handler
        if description is not None:
            input_["description"] = description
        if timeout is not None:
            input_["timeout"] = timeout
        if memory_size is not None:
            input_["memory_size"] = memory_size
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if environment is not None:
            input_["environment"] = environment
        if runtime is not None:
            input_["runtime"] = runtime
        if dead_letter_config is not None:
            input_["dead_letter_config"] = dead_letter_config
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tracing_config is not None:
            input_["tracing_config"] = tracing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if layers is not None:
            input_["layers"] = layers
        if file_system_configs is not None:
            input_["file_system_configs"] = file_system_configs
        if image_config is not None:
            input_["image_config"] = image_config
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if snap_start is not None:
            input_["snap_start"] = snap_start
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if capacity_provider_config is not None:
            input_["capacity_provider_config"] = capacity_provider_config
        if durable_config is not None:
            input_["durable_config"] = durable_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        auth_type: "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse":
        r"""<p>Creates a Lambda function URL with the specified configuration parameters. A function URL is a dedicated HTTP(S) endpoint that you can use to invoke your function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.create_function_url_config_response.CreateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_function_url_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_function_url_config.async_create_function_url_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_function_url_config_request.CreateFunctionUrlConfigRequest = {
            "function_name": function_name,
            "auth_type": auth_type,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> None:
        r"""<p>Removes the code signing configuration from the function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_function_code_signing_config.async_delete_function_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_code_signing_config_request.DeleteFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> None:
        r"""<p>Deletes a Lambda function URL. When you delete a function URL, you can't recover it. Creating a new function URL results in a different URL address.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_function_url_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_function_url_config.async_delete_function_url_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_function_url_config_request.DeleteFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_response.GetFunctionResponse":
        r"""<p>Returns information about the function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details that are specific to that version are returned.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function
            The following example returns code and configuration details for version 1 of a function named my-function.

            >>> await client.get_function(function_name='my-function', qualifier='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_request.GetFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function.async_get_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_request.GetFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_code_signing_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse":
        r"""<p>Returns the code signing configuration for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_code_signing_config_response.GetFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_code_signing_config.async_get_function_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_code_signing_config_request.GetFunctionCodeSigningConfigRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_configuration(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        r"""<p>Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use <a>UpdateFunctionConfiguration</a>.</p> <p>To get all of a function's details, including function-level settings, use <a>GetFunction</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get details about a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function's event source mapping
            The following example returns and configuration details for version 1 of a function named my-function.

            >>> await client.get_function_configuration(function_name='my-function', qualifier='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_configuration

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_configuration.async_get_function_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_configuration_request.GetFunctionConfigurationRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse":
        r"""<p>Returns your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration. </p>

        Args:
            function_name: <p>The name of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_recursion_config_response.GetFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_recursion_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_recursion_config.async_get_function_recursion_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_recursion_config_request.GetFunctionRecursionConfigRequest = {
            "function_name": function_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse":
        """<p>Retrieves the scaling configuration for a Lambda Managed Instances function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to get the scaling configuration for a published version of the function.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_scaling_config_response.GetFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_scaling_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_scaling_config.async_get_function_scaling_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_scaling_config_request.GetFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse":
        r"""<p>Returns details about a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_function_url_config_response.GetFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_function_url_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_function_url_config.async_get_function_url_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_function_url_config_request.GetFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_policy(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_policy_response.GetPolicyResponse":
        r"""<p>Returns the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html\">resource-based IAM policy</a> for a function, version, or alias.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version or alias to get the policy for that resource.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve a Lambda function policy
            The following example returns the resource-based policy for version 1 of a Lambda function named my-function.

            >>> await client.get_policy(function_name='my-function', qualifier='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_policy

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_policy_request.GetPolicyRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
    ) -> "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse":
        r"""<p>Retrieves the runtime management configuration for a function's version. If the runtime update mode is <b>Manual</b>, this includes the ARN of the runtime version and the runtime update mode. If the runtime update mode is <b>Auto</b> or <b>Function update</b>, this includes the runtime update mode and <code>null</code> is returned for the ARN. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_runtime_management_config_response.GetRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_runtime_management_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_runtime_management_config.async_get_runtime_management_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_runtime_management_config_request.GetRuntimeManagementConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        invocation_type: Optional[
            "capo_lambda.types.invocation_type.InvocationType"
        ] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
    ) -> "capo_lambda.types.invocation_response.InvocationResponse":
        r"""<p>Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the<code>InvocationType</code> is <code>RequestResponse</code>). To invoke a function asynchronously, set <code>InvocationType</code> to <code>Event</code>. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p> <p>For synchronous invocations, the maximum payload size is 6 MB. For asynchronous invocations, the maximum payload size is 1 MB.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html\">synchronous invocation</a>, details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html\">execution log</a> and <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html\">trace</a>.</p> <p>When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html\">Error handling and automatic retries in Lambda</a>.</p> <p>For <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html\">asynchronous invocation</a>, Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">dead-letter queue</a>.</p> <p>The status code in the API response doesn't reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">quota</a> errors, or issues with your function's code and configuration. For example, Lambda returns <code>TooManyRequestsException</code> if running the function would cause you to exceed a concurrency limit at either the account level (<code>ConcurrentInvocationLimitExceeded</code>) or function level (<code>ReservedFunctionConcurrentInvocationLimitExceeded</code>).</p> <p>For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function, version, or alias.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invocation_type: <p>Choose from the following options.</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.</p> </li> <li> <p> <code>Event</code> – Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if one is configured). The API response only includes a status code.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the user or role has permission to invoke the function.</p> </li> </ul>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the <code>ClientContext</code> object to your function for synchronous invocations only.</p>
            durable_execution_name: <p>A unique name for the durable execution. If you invoke a durable function using a name that already exists with the same payload, Lambda returns the existing execution instead of creating a duplicate. If the payload differs, Lambda returns a <code>DurableExecutionAlreadyStartedException</code> error.</p> <p>If not specified, Lambda generates a unique identifier automatically. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-execution-idempotency.html#durable-idempotency-execution-names\">Execution names</a>.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input. The maximum payload size is 6 MB for synchronous invocations and 1 MB for asynchronous invocations.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            qualifier: <p>Specify a version or alias to invoke a published version of the function.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>

        Raises:
            capo_lambda.errors.code_artifact_user_deleted_exception.CodeArtifactUserDeletedException: <p>The Lambda function couldn't be invoked because its code artifact user has been deleted. Wait for Lambda to provision a new code artifact user, or update the function's code package to recreate it.</p>
            capo_lambda.errors.code_artifact_user_failed_exception.CodeArtifactUserFailedException: <p>The Lambda function couldn't be invoked because provisioning of its code artifact user failed. Update the function's code package or check the Lambda function's <code>State</code> and <code>StateReasonCode</code> for additional context.</p>
            capo_lambda.errors.code_artifact_user_pending_exception.CodeArtifactUserPendingException: <p>The Lambda function couldn't be invoked because its code artifact user is still being provisioned. Wait for the function's <code>State</code> to become <code>Active</code> and try the request again.</p>
            capo_lambda.errors.durable_execution_already_started_exception.DurableExecutionAlreadyStartedException: <p>The durable execution with the specified name has already been started. Each durable execution name must be unique within the function. Use a different name or check the status of the existing execution.</p>
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.eni_not_ready_exception.ENINotReadyException: <p>Lambda couldn't invoke the Lambda function because the elastic network interface (ENI) configured for its VPC connection isn't ready yet. Wait a few moments and try the request again. For more information about VPC configuration, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function
            The following example invokes version 1 of a function named my-function with an empty event payload.

            >>> await client.invoke(durable_execution_name='myExecution', function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
            To invoke a Lambda function asynchronously
            The following example invokes version 1 of a function named my-function asynchronously.

            >>> await client.invoke(function_name='my-function', invocation_type='Event', payload='{}', qualifier='1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.invocation_request.InvocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.invocation_response.InvocationResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.invoke.async_invoke(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invocation_request.InvocationRequest = {
            "function_name": function_name
        }
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if payload is not None:
            input_["payload"] = payload
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke_async(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        invoke_args: Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes,
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.invoke_async_response.InvokeAsyncResponse":
        r"""<note> <p>For asynchronous function invocation, use <a>Invoke</a>.</p> </note> <p>Invokes a function asynchronously.</p> <note> <p>The payload limit is 256KB. For larger payloads, for up to 1MB, use <a>Invoke</a>.</p> </note> <note> <p>If you do use the InvokeAsync action, note that it doesn't support the use of X-Ray active tracing. Trace ID is not propagated to the function, even if X-Ray active tracing is turned on.</p> </note>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            invoke_args: <p>The JSON that you want to provide to your Lambda function as input.</p>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.mode_not_supported_exception.ModeNotSupportedException: <p>The Lambda function doesn't support the invocation mode requested. For example, calling <code>Invoke</code> with <code>InvocationType=RequestResponse</code> on a function configured for asynchronous-only invocation, or vice versa. For more information about invocation types, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html\">Invoking Lambda functions</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To invoke a Lambda function asynchronously
            The following example invokes a Lambda function asynchronously

            >>> await client.invoke_async(function_name='my-function', invoke_args='{}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.invoke_async_request.InvokeAsyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.invoke_async_response.InvokeAsyncResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_async

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.invoke_async.async_invoke_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_async_request.InvokeAsyncRequest = {
            "function_name": function_name,
            "invoke_args": ensure_async_iterator(invoke_args),
        }

        async with aclosing_bodies(input_):
            response = await aexecute_pipeline(
                AsyncOperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            await response.response.aclose()
            return response.output

    @asynccontextmanager
    async def invoke_with_response_stream(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        log_type: Optional["capo_lambda.types.log_type.LogType"] = None,
        client_context: Optional["capo_lambda.types.string.String"] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        payload: Optional["capo_lambda.types.blob.Blob"] = None,
        tenant_id: Optional["capo_lambda.types.tenant_id.TenantId"] = None,
        invocation_type: Optional[
            "capo_lambda.types.response_streaming_invocation_type.ResponseStreamingInvocationType"
        ] = None,
    ) -> "AsyncGenerator[capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse]":
        r"""<p>Configure your Lambda functions to stream response payloads back to clients. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html\">Configuring a Lambda function to stream responses</a>.</p> <p>This operation requires permission for the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html\">lambda:InvokeFunction</a> action. For details on how to set up permissions for cross-account invocations, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke\">Granting function access to other accounts</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            log_type: <p>Set to <code>Tail</code> to include the execution log in the response. Applies to synchronously invoked functions only.</p>
            client_context: <p>Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.</p>
            qualifier: <p>The alias name.</p>
            payload: <p>The JSON that you want to provide to your Lambda function as input.</p> <p>You can enter the JSON directly. For example, <code>--payload '{ \"key\": \"value\" }'</code>. You can also specify a file path. For example, <code>--payload file://payload.json</code>.</p>
            tenant_id: <p>The identifier of the tenant in a multi-tenant Lambda function.</p>
            invocation_type: <p>Use one of the following options:</p> <ul> <li> <p> <code>RequestResponse</code> (default) – Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API operation response includes the function response and additional data.</p> </li> <li> <p> <code>DryRun</code> – Validate parameter values and verify that the IAM user or role has permission to invoke the function.</p> </li> </ul>

        Raises:
            capo_lambda.errors.ec2_access_denied_exception.EC2AccessDeniedException: <p>Need additional permissions to configure VPC settings.</p>
            capo_lambda.errors.ec2_throttled_exception.EC2ThrottledException: <p>Amazon EC2 throttled Lambda during Lambda function initialization using the execution role provided for the function.</p>
            capo_lambda.errors.ec2_unexpected_exception.EC2UnexpectedException: <p>Lambda received an unexpected Amazon EC2 client exception while setting up for the Lambda function.</p>
            capo_lambda.errors.efsio_exception.EFSIOException: <p>An error occurred when reading from or writing to a connected file system.</p>
            capo_lambda.errors.efs_mount_connectivity_exception.EFSMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured file system.</p>
            capo_lambda.errors.efs_mount_failure_exception.EFSMountFailureException: <p>The Lambda function couldn't mount the configured file system due to a permission or configuration issue.</p>
            capo_lambda.errors.efs_mount_timeout_exception.EFSMountTimeoutException: <p>The Lambda function made a network connection to the configured file system, but the mount operation timed out.</p>
            capo_lambda.errors.eni_limit_reached_exception.ENILimitReachedException: <p>Lambda couldn't create an elastic network interface in the VPC, specified as part of Lambda function configuration, because the limit for network interfaces has been reached. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.invalid_request_content_exception.InvalidRequestContentException: <p>The request body could not be parsed as JSON, or a request header is invalid. For example, the 'x-amzn-RequestId' header is not a valid UUID string.</p>
            capo_lambda.errors.invalid_runtime_exception.InvalidRuntimeException: <p>The runtime or runtime version specified is not supported.</p>
            capo_lambda.errors.invalid_security_group_id_exception.InvalidSecurityGroupIDException: <p>The security group ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_subnet_id_exception.InvalidSubnetIDException: <p>The subnet ID provided in the Lambda function VPC configuration is not valid.</p>
            capo_lambda.errors.invalid_zip_file_exception.InvalidZipFileException: <p>Lambda could not unzip the deployment package.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.no_published_version_exception.NoPublishedVersionException: <p>The function has no published versions available.</p>
            capo_lambda.errors.recursive_invocation_exception.RecursiveInvocationException: <p>Lambda has detected your function being invoked in a recursive loop with other Amazon Web Services resources and stopped your function's invocation.</p>
            capo_lambda.errors.request_too_large_exception.RequestTooLargeException: <p>The request payload exceeded the <code>Invoke</code> request body JSON input quota. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.resource_not_ready_exception.ResourceNotReadyException: <p>The function is inactive and its VPC connection is no longer available. Wait for the VPC connection to reestablish and try again.</p>
            capo_lambda.errors.s3_files_mount_connectivity_exception.S3FilesMountConnectivityException: <p>The Lambda function couldn't make a network connection to the configured S3 Files access point.</p>
            capo_lambda.errors.s3_files_mount_failure_exception.S3FilesMountFailureException: <p>The Lambda function couldn't mount the configured S3 Files access point due to a permission or configuration issue.</p>
            capo_lambda.errors.s3_files_mount_timeout_exception.S3FilesMountTimeoutException: <p>The Lambda function made a network connection to the configured S3 Files access point, but the mount operation timed out.</p>
            capo_lambda.errors.serialized_request_entity_too_large_exception.SerializedRequestEntityTooLargeException: <p>The request payload exceeded the maximum allowed size for serialized request entities.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota. For more information about Lambda service quotas, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html\">Lambda quotas</a>. To request a quota increase, see <a href=\"https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html\">Requesting a quota increase</a> in the <i>Service Quotas User Guide</i>.</p>
            capo_lambda.errors.snap_start_exception.SnapStartException: <p>The <code>afterRestore()</code> <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html\">runtime hook</a> encountered an error. For more information, check the Amazon CloudWatch logs.</p>
            capo_lambda.errors.snap_start_not_ready_exception.SnapStartNotReadyException: <p>Lambda is initializing your function. You can invoke the function when the <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html\">function state</a> becomes <code>Active</code>.</p>
            capo_lambda.errors.snap_start_regeneration_failure_exception.SnapStartRegenerationFailureException: <p>Lambda couldn't regenerate the SnapStart snapshot for the function. SnapStart-enabled functions periodically regenerate snapshots when their underlying runtime or dependencies change; this regeneration failed. Wait for Lambda to retry, or update the function's configuration to trigger a new snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Lambda SnapStart</a>.</p>
            capo_lambda.errors.snap_start_timeout_exception.SnapStartTimeoutException: <p>Lambda couldn't restore the snapshot within the timeout limit.</p>
            capo_lambda.errors.subnet_ip_address_limit_reached_exception.SubnetIPAddressLimitReachedException: <p>Lambda couldn't set up VPC access for the Lambda function because one or more configured subnets has no available IP addresses.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The content type of the <code>Invoke</code> request body is not JSON.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.invoke_with_response_stream.async_invoke_with_response_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest = {
            "function_name": function_name
        }
        if log_type is not None:
            input_["log_type"] = log_type
        if client_context is not None:
            input_["client_context"] = client_context
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if payload is not None:
            input_["payload"] = payload
        if tenant_id is not None:
            input_["tenant_id"] = tenant_id
        if invocation_type is not None:
            input_["invocation_type"] = invocation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def list_durable_executions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        durable_execution_name: Optional[
            "capo_lambda.types.durable_execution_name.DurableExecutionName"
        ] = None,
        statuses: Optional[
            "capo_lambda.types.execution_status_list.ExecutionStatusList"
        ] = None,
        started_after: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        started_before: Optional[
            "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
        ] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse":
        r"""<p>Returns a list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html\">durable executions</a> for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.</p>
            qualifier: <p>The function version or alias. If not specified, lists executions for the $LATEST version.</p>
            durable_execution_name: <p>Filter executions by name. Only executions with names that matches this string are returned.</p>
            statuses: <p>Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED_OUT, STOPPED.</p>
            started_after: <p>Filter executions that started after this timestamp (ISO 8601 format).</p>
            started_before: <p>Filter executions that started before this timestamp (ISO 8601 format).</p>
            reverse_order: <p>Set to true to return results in chronological order (oldest first). Default is false.</p>
            marker: <p>Pagination token from a previous request to continue retrieving results.</p>
            max_items: <p>Maximum number of executions to return (1-1000). Default is 100.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_durable_executions_by_function_response.ListDurableExecutionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_durable_executions_by_function.async_list_durable_executions_by_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_durable_executions_by_function_request.ListDurableExecutionsByFunctionRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if durable_execution_name is not None:
            input_["durable_execution_name"] = durable_execution_name
        if statuses is not None:
            input_["statuses"] = statuses
        if started_after is not None:
            input_["started_after"] = started_after
        if started_before is not None:
            input_["started_before"] = started_before
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_function_url_configs(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_items.MaxItems"] = None,
    ) -> "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse":
        r"""<p>Returns a list of Lambda function URLs for the specified function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of function URLs to return in the response. Note that <code>ListFunctionUrlConfigs</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_function_url_configs_response.ListFunctionUrlConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_function_url_configs

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_function_url_configs.async_list_function_url_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_function_url_configs_request.ListFunctionUrlConfigsRequest = {
            "function_name": function_name
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_function_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse":
        r"""<p>Update the code signing configuration for the function. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda.errors.code_signing_config_not_found_exception.CodeSigningConfigNotFoundException: <p>The specified code signing configuration does not exist.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.put_function_code_signing_config_response.PutFunctionCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_function_code_signing_config.async_put_function_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_code_signing_config_request.PutFunctionCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn,
            "function_name": function_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_function_recursion_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        recursive_loop: "capo_lambda.types.recursive_loop.RecursiveLoop",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse":
        r"""<p>Sets your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html\">recursive loop detection</a> configuration.</p> <p>When you configure a Lambda function to output to the same service or resource that invokes the function, it's possible to create an infinite recursive loop. For example, a Lambda function might write a message to an Amazon Simple Queue Service (Amazon SQS) queue, which then invokes the same function. This invocation causes the function to write another message to the queue, which in turn invokes the function again.</p> <p>Lambda can detect certain types of recursive loops shortly after they occur. When Lambda detects a recursive loop and your function's recursive loop detection configuration is set to <code>Terminate</code>, it stops your function being invoked and notifies you.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            recursive_loop: <p>If you set your function's recursive loop detection configuration to <code>Allow</code>, Lambda doesn't take any action when it detects your function being invoked as part of a recursive loop. We recommend that you only use this setting if your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes it.</p> <p>If you set your function's recursive loop detection configuration to <code>Terminate</code>, Lambda stops your function being invoked and notifies you when it detects your function being invoked as part of a recursive loop.</p> <p>By default, Lambda sets your function's configuration to <code>Terminate</code>.</p> <important> <p>If your design intentionally uses a Lambda function to write data back to the same Amazon Web Services resource that invokes the function, then use caution and implement suitable guard rails to prevent unexpected charges being billed to your Amazon Web Services account. To learn more about best practices for using recursive invocation patterns, see <a href=\"https://serverlessland.com/content/service/lambda/guides/aws-lambda-operator-guide/recursive-runaway\">Recursive patterns that cause run-away Lambda functions</a> in Serverless Land.</p> </important>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.put_function_recursion_config_response.PutFunctionRecursionConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_recursion_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_function_recursion_config.async_put_function_recursion_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_recursion_config_request.PutFunctionRecursionConfigRequest = {
            "function_name": function_name,
            "recursive_loop": recursive_loop,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_function_scaling_config(
        self,
        function_name: "capo_lambda.types.unqualified_function_name.UnqualifiedFunctionName",
        qualifier: "capo_lambda.types.published_function_qualifier.PublishedFunctionQualifier",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        function_scaling_config: Optional[
            "capo_lambda.types.function_scaling_config.FunctionScalingConfig"
        ] = None,
    ) -> "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse":
        """<p>Sets the scaling configuration for a Lambda Managed Instances function. The scaling configuration defines the minimum and maximum number of execution environments that can be provisioned for the function, allowing you to control scaling behavior and resource allocation.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p>
            qualifier: <p>Specify a version or alias to set the scaling configuration for a published version of the function.</p>
            function_scaling_config: <p>The scaling configuration to apply to the function, including minimum and maximum execution environment limits.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.put_function_scaling_config_response.PutFunctionScalingConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_function_scaling_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_function_scaling_config.async_put_function_scaling_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_function_scaling_config_request.PutFunctionScalingConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }
        if function_scaling_config is not None:
            input_["function_scaling_config"] = function_scaling_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_runtime_management_config(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        update_runtime_on: "capo_lambda.types.update_runtime_on.UpdateRuntimeOn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
        ] = None,
        runtime_version_arn: Optional[
            "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
        ] = None,
    ) -> "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse":
        r"""<p>Sets the runtime management configuration for a function's version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html\">Runtime updates</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>Specify a version of the function. This can be <code>$LATEST</code> or a published version number. If no value is specified, the configuration for the <code>$LATEST</code> version is returned.</p>
            update_runtime_on: <p>Specify the runtime update mode.</p> <ul> <li> <p> <b>Auto (default)</b> - Automatically update to the most recent and secure runtime version using a <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-two-phase\">Two-phase runtime version rollout</a>. This is the best choice for most customers to ensure they always benefit from runtime updates.</p> </li> <li> <p> <b>Function update</b> - Lambda updates the runtime of your function to the most recent and secure runtime version when you update your function. This approach synchronizes runtime updates with function deployments, giving you control over when runtime updates are applied and allowing you to detect and mitigate rare runtime update incompatibilities early. When using this setting, you need to regularly update your functions to keep their runtime up-to-date.</p> </li> <li> <p> <b>Manual</b> - You specify a runtime version in your function configuration. The function will use this runtime version indefinitely. In the rare case where a new runtime version is incompatible with an existing function, this allows you to roll back your function to an earlier runtime version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-rollback\">Roll back a runtime version</a>.</p> </li> </ul>
            runtime_version_arn: <p>The ARN of the runtime version you want the function to use.</p> <note> <p>This is only required if you're using the <b>Manual</b> runtime update mode.</p> </note>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.put_runtime_management_config_response.PutRuntimeManagementConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_runtime_management_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_runtime_management_config.async_put_runtime_management_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_runtime_management_config_request.PutRuntimeManagementConfigRequest = {
            "function_name": function_name,
            "update_runtime_on": update_runtime_on,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if runtime_version_arn is not None:
            input_["runtime_version_arn"] = runtime_version_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_function_url_config(
        self,
        function_name: "capo_lambda.types.function_url_function_name.FunctionUrlFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        qualifier: Optional[
            "capo_lambda.types.function_url_qualifier.FunctionUrlQualifier"
        ] = None,
        auth_type: Optional[
            "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
        ] = None,
        cors: Optional["capo_lambda.types.cors.Cors"] = None,
        invoke_mode: Optional["capo_lambda.types.invoke_mode.InvokeMode"] = None,
    ) -> "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse":
        r"""<p>Updates the configuration for a Lambda function URL.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The alias name.</p>
            auth_type: <p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html\">Control access to Lambda function URLs</a>.</p>
            cors: <p>The <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS\">cross-origin resource sharing (CORS)</a> settings for your function URL.</p>
            invoke_mode: <p>Use one of the following options:</p> <ul> <li> <p> <code>BUFFERED</code> – This is the default option. Lambda invokes your function using the <code>Invoke</code> API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.</p> </li> <li> <p> <code>RESPONSE_STREAM</code> – Your function streams payload results as they become available. Lambda invokes your function using the <code>InvokeWithResponseStream</code> API operation. The maximum response payload size is 200 MB.</p> </li> </ul>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests\">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.update_function_url_config_response.UpdateFunctionUrlConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_function_url_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_function_url_config.async_update_function_url_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_function_url_config_request.UpdateFunctionUrlConfigRequest = {
            "function_name": function_name
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if cors is not None:
            input_["cors"] = cors
        if invoke_mode is not None:
            input_["invoke_mode"] = invoke_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
