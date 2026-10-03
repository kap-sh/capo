"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateFunctionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider_config
    import capo_lambda.types.dead_letter_config
    import capo_lambda.types.description
    import capo_lambda.types.durable_config
    import capo_lambda.types.environment
    import capo_lambda.types.ephemeral_storage
    import capo_lambda.types.file_system_config_list
    import capo_lambda.types.function_name
    import capo_lambda.types.handler
    import capo_lambda.types.image_config
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.layer_list
    import capo_lambda.types.logging_config
    import capo_lambda.types.memory_size
    import capo_lambda.types.role_arn
    import capo_lambda.types.runtime
    import capo_lambda.types.snap_start
    import capo_lambda.types.string
    import capo_lambda.types.timeout
    import capo_lambda.types.tracing_config
    import capo_lambda.types.vpc_config


class UpdateFunctionConfigurationRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    role: NotRequired["capo_lambda.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the function's execution role.</p>"""
    handler: NotRequired["capo_lambda.types.handler.Handler"]
    """<p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html">Lambda programming model</a>.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>A description of the function.</p>"""
    timeout: NotRequired["capo_lambda.types.timeout.Timeout"]
    """<p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds, and the maximum allowed value is 900 seconds. For functions using Lambda Managed Instances, asynchronous invocations and event source mapping invocations (except Amazon MQ and Amazon DocumentDB) support a maximum allowed value of 5,400 seconds (90 minutes). For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html">Lambda execution environment</a>.</p>"""
    memory_size: NotRequired["capo_lambda.types.memory_size.MemorySize"]
    """<p>The amount of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>"""
    vpc_config: NotRequired["capo_lambda.types.vpc_config.VpcConfig"]
    """<p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html">Configuring a Lambda function to access resources in a VPC</a>.</p>"""
    environment: NotRequired["capo_lambda.types.environment.Environment"]
    """<p>Environment variables that are accessible from function code during execution.</p>"""
    runtime: NotRequired["capo_lambda.types.runtime.Runtime"]
    """<p>The identifier of the function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported">Supported runtimes</a>.</p>"""
    dead_letter_config: NotRequired[
        "capo_lambda.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq">Dead-letter queues</a>.</p>"""
    kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption">environment variables</a>.</p> </li> <li> <p>The function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk">Amazon Web Services owned key</a> or an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk">Amazon Web Services managed key</a>.</p>"""
    tracing_config: NotRequired["capo_lambda.types.tracing_config.TracingConfig"]
    """<p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href="https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html">X-Ray</a>.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Update the function only if the revision ID matches the ID that's specified. Use this option to avoid modifying a function that has changed since you last read it.</p>"""
    layers: NotRequired["capo_lambda.types.layer_list.LayerList"]
    """<p>A list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>"""
    file_system_configs: NotRequired[
        "capo_lambda.types.file_system_config_list.FileSystemConfigList"
    ]
    """<p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>"""
    image_config: NotRequired["capo_lambda.types.image_config.ImageConfig"]
    """<p> <a href="https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms">Container image configuration values</a> that override the values in the container image Docker file.</p>"""
    ephemeral_storage: NotRequired[
        "capo_lambda.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage">Configuring ephemeral storage (console)</a>.</p>"""
    snap_start: NotRequired["capo_lambda.types.snap_start.SnapStart"]
    """<p>The function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html">SnapStart</a> setting.</p>"""
    logging_config: NotRequired["capo_lambda.types.logging_config.LoggingConfig"]
    """<p>The function's Amazon CloudWatch Logs configuration settings.</p>"""
    capacity_provider_config: NotRequired[
        "capo_lambda.types.capacity_provider_config.CapacityProviderConfig"
    ]
    """<p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>"""
    durable_config: NotRequired["capo_lambda.types.durable_config.DurableConfig"]
    """<p>Configuration settings for <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable functions</a>, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFunctionConfigurationRequest) -> dict:
    out: dict = {}
    if "role" in value:
        out["Role"] = value["role"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    if "description" in value:
        out["Description"] = value["description"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    if "vpc_config" in value:
        import capo_lambda.types.vpc_config

        out["VpcConfig"] = capo_lambda.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "environment" in value:
        import capo_lambda.types.environment

        out["Environment"] = capo_lambda.types.environment.serialize_json(
            value["environment"]
        )
    if "runtime" in value:
        import capo_lambda.types.runtime

        out["Runtime"] = capo_lambda.types.runtime.serialize_json(value["runtime"])
    if "dead_letter_config" in value:
        import capo_lambda.types.dead_letter_config

        out["DeadLetterConfig"] = capo_lambda.types.dead_letter_config.serialize_json(
            value["dead_letter_config"]
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "tracing_config" in value:
        import capo_lambda.types.tracing_config

        out["TracingConfig"] = capo_lambda.types.tracing_config.serialize_json(
            value["tracing_config"]
        )
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "layers" in value:
        import capo_lambda.types.layer_list

        out["Layers"] = capo_lambda.types.layer_list.serialize_json(value["layers"])
    if "file_system_configs" in value:
        import capo_lambda.types.file_system_config_list

        out["FileSystemConfigs"] = (
            capo_lambda.types.file_system_config_list.serialize_json(
                value["file_system_configs"]
            )
        )
    if "image_config" in value:
        import capo_lambda.types.image_config

        out["ImageConfig"] = capo_lambda.types.image_config.serialize_json(
            value["image_config"]
        )
    if "ephemeral_storage" in value:
        import capo_lambda.types.ephemeral_storage

        out["EphemeralStorage"] = capo_lambda.types.ephemeral_storage.serialize_json(
            value["ephemeral_storage"]
        )
    if "snap_start" in value:
        import capo_lambda.types.snap_start

        out["SnapStart"] = capo_lambda.types.snap_start.serialize_json(
            value["snap_start"]
        )
    if "logging_config" in value:
        import capo_lambda.types.logging_config

        out["LoggingConfig"] = capo_lambda.types.logging_config.serialize_json(
            value["logging_config"]
        )
    if "capacity_provider_config" in value:
        import capo_lambda.types.capacity_provider_config

        out["CapacityProviderConfig"] = (
            capo_lambda.types.capacity_provider_config.serialize_json(
                value["capacity_provider_config"]
            )
        )
    if "durable_config" in value:
        import capo_lambda.types.durable_config

        out["DurableConfig"] = capo_lambda.types.durable_config.serialize_json(
            value["durable_config"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFunctionConfigurationRequest:
    out: UpdateFunctionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("Handler") is not None:
        out["handler"] = data["Handler"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("MemorySize") is not None:
        out["memory_size"] = data["MemorySize"]
    if data.get("VpcConfig") is not None:
        import capo_lambda.types.vpc_config

        out["vpc_config"] = capo_lambda.types.vpc_config.deserialize_json(
            data["VpcConfig"]
        )
    if data.get("Environment") is not None:
        import capo_lambda.types.environment

        out["environment"] = capo_lambda.types.environment.deserialize_json(
            data["Environment"]
        )
    if data.get("Runtime") is not None:
        import capo_lambda.types.runtime

        out["runtime"] = capo_lambda.types.runtime.deserialize_json(data["Runtime"])
    if data.get("DeadLetterConfig") is not None:
        import capo_lambda.types.dead_letter_config

        out["dead_letter_config"] = (
            capo_lambda.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if data.get("TracingConfig") is not None:
        import capo_lambda.types.tracing_config

        out["tracing_config"] = capo_lambda.types.tracing_config.deserialize_json(
            data["TracingConfig"]
        )
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("Layers") is not None:
        import capo_lambda.types.layer_list

        out["layers"] = capo_lambda.types.layer_list.deserialize_json(data["Layers"])
    if data.get("FileSystemConfigs") is not None:
        import capo_lambda.types.file_system_config_list

        out["file_system_configs"] = (
            capo_lambda.types.file_system_config_list.deserialize_json(
                data["FileSystemConfigs"]
            )
        )
    if data.get("ImageConfig") is not None:
        import capo_lambda.types.image_config

        out["image_config"] = capo_lambda.types.image_config.deserialize_json(
            data["ImageConfig"]
        )
    if data.get("EphemeralStorage") is not None:
        import capo_lambda.types.ephemeral_storage

        out["ephemeral_storage"] = capo_lambda.types.ephemeral_storage.deserialize_json(
            data["EphemeralStorage"]
        )
    if data.get("SnapStart") is not None:
        import capo_lambda.types.snap_start

        out["snap_start"] = capo_lambda.types.snap_start.deserialize_json(
            data["SnapStart"]
        )
    if data.get("LoggingConfig") is not None:
        import capo_lambda.types.logging_config

        out["logging_config"] = capo_lambda.types.logging_config.deserialize_json(
            data["LoggingConfig"]
        )
    if data.get("CapacityProviderConfig") is not None:
        import capo_lambda.types.capacity_provider_config

        out["capacity_provider_config"] = (
            capo_lambda.types.capacity_provider_config.deserialize_json(
                data["CapacityProviderConfig"]
            )
        )
    if data.get("DurableConfig") is not None:
        import capo_lambda.types.durable_config

        out["durable_config"] = capo_lambda.types.durable_config.deserialize_json(
            data["DurableConfig"]
        )
    return out
