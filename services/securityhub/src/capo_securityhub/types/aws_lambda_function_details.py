"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_lambda_function_code
    import capo_securityhub.types.aws_lambda_function_dead_letter_config
    import capo_securityhub.types.aws_lambda_function_environment
    import capo_securityhub.types.aws_lambda_function_layer_list
    import capo_securityhub.types.aws_lambda_function_tracing_config
    import capo_securityhub.types.aws_lambda_function_vpc_config
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsLambdaFunctionDetails(TypedDict, closed=True):
    code: NotRequired[
        "capo_securityhub.types.aws_lambda_function_code.AwsLambdaFunctionCode"
    ]
    """<p>An <code>AwsLambdaFunctionCode</code> object.</p>"""
    code_sha256: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The SHA256 hash of the function's deployment package.</p>"""
    dead_letter_config: NotRequired[
        "capo_securityhub.types.aws_lambda_function_dead_letter_config.AwsLambdaFunctionDeadLetterConfig"
    ]
    """<p>The function's dead letter queue.</p>"""
    environment: NotRequired[
        "capo_securityhub.types.aws_lambda_function_environment.AwsLambdaFunctionEnvironment"
    ]
    """<p>The function's environment variables.</p>"""
    function_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the function.</p>"""
    handler: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The function that Lambda calls to begin executing your function.</p>"""
    kms_key_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key that is used to encrypt the function's environment variables. This key is only returned if you've configured a customer managed customer managed key.</p>"""
    last_modified: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the function was last updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    layers: NotRequired[
        "capo_securityhub.types.aws_lambda_function_layer_list.AwsLambdaFunctionLayerList"
    ]
    """<p>The function's layers.</p>"""
    master_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>For Lambda@Edge functions, the ARN of the master function.</p>"""
    memory_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The memory that is allocated to the function.</p>"""
    revision_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The latest updated revision of the function or alias.</p>"""
    role: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The function's execution role.</p>"""
    runtime: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The runtime environment for the Lambda function.</p>"""
    timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The amount of time that Lambda allows a function to run before stopping it.</p>"""
    tracing_config: NotRequired[
        "capo_securityhub.types.aws_lambda_function_tracing_config.AwsLambdaFunctionTracingConfig"
    ]
    """<p>The function's X-Ray tracing configuration.</p>"""
    vpc_config: NotRequired[
        "capo_securityhub.types.aws_lambda_function_vpc_config.AwsLambdaFunctionVpcConfig"
    ]
    """<p>The function's networking configuration.</p>"""
    version: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of the Lambda function.</p>"""
    architectures: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The instruction set architecture that the function uses. Valid values are <code>x86_64</code> or <code>arm64</code>.</p>"""
    package_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of deployment package that's used to deploy the function code to Lambda. Set to <code>Image</code> for a container image and <code>Zip</code> for a .zip file archive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionDetails) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_securityhub.types.aws_lambda_function_code

        out["Code"] = capo_securityhub.types.aws_lambda_function_code.serialize_json(
            value["code"]
        )
    if "code_sha256" in value:
        out["CodeSha256"] = value["code_sha256"]
    if "dead_letter_config" in value:
        import capo_securityhub.types.aws_lambda_function_dead_letter_config

        out["DeadLetterConfig"] = (
            capo_securityhub.types.aws_lambda_function_dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "environment" in value:
        import capo_securityhub.types.aws_lambda_function_environment

        out["Environment"] = (
            capo_securityhub.types.aws_lambda_function_environment.serialize_json(
                value["environment"]
            )
        )
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "layers" in value:
        import capo_securityhub.types.aws_lambda_function_layer_list

        out["Layers"] = (
            capo_securityhub.types.aws_lambda_function_layer_list.serialize_json(
                value["layers"]
            )
        )
    if "master_arn" in value:
        out["MasterArn"] = value["master_arn"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "role" in value:
        out["Role"] = value["role"]
    if "runtime" in value:
        out["Runtime"] = value["runtime"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "tracing_config" in value:
        import capo_securityhub.types.aws_lambda_function_tracing_config

        out["TracingConfig"] = (
            capo_securityhub.types.aws_lambda_function_tracing_config.serialize_json(
                value["tracing_config"]
            )
        )
    if "vpc_config" in value:
        import capo_securityhub.types.aws_lambda_function_vpc_config

        out["VpcConfig"] = (
            capo_securityhub.types.aws_lambda_function_vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "architectures" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Architectures"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["architectures"]
            )
        )
    if "package_type" in value:
        out["PackageType"] = value["package_type"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionDetails:
    out: AwsLambdaFunctionDetails = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_securityhub.types.aws_lambda_function_code

        out["code"] = capo_securityhub.types.aws_lambda_function_code.deserialize_json(
            data["Code"]
        )
    if data.get("CodeSha256") is not None:
        out["code_sha256"] = data["CodeSha256"]
    if data.get("DeadLetterConfig") is not None:
        import capo_securityhub.types.aws_lambda_function_dead_letter_config

        out["dead_letter_config"] = (
            capo_securityhub.types.aws_lambda_function_dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if data.get("Environment") is not None:
        import capo_securityhub.types.aws_lambda_function_environment

        out["environment"] = (
            capo_securityhub.types.aws_lambda_function_environment.deserialize_json(
                data["Environment"]
            )
        )
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    if data.get("Handler") is not None:
        out["handler"] = data["Handler"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    if data.get("Layers") is not None:
        import capo_securityhub.types.aws_lambda_function_layer_list

        out["layers"] = (
            capo_securityhub.types.aws_lambda_function_layer_list.deserialize_json(
                data["Layers"]
            )
        )
    if data.get("MasterArn") is not None:
        out["master_arn"] = data["MasterArn"]
    if data.get("MemorySize") is not None:
        out["memory_size"] = data["MemorySize"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("Runtime") is not None:
        out["runtime"] = data["Runtime"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("TracingConfig") is not None:
        import capo_securityhub.types.aws_lambda_function_tracing_config

        out["tracing_config"] = (
            capo_securityhub.types.aws_lambda_function_tracing_config.deserialize_json(
                data["TracingConfig"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_securityhub.types.aws_lambda_function_vpc_config

        out["vpc_config"] = (
            capo_securityhub.types.aws_lambda_function_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Architectures") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["architectures"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Architectures"]
            )
        )
    if data.get("PackageType") is not None:
        out["package_type"] = data["PackageType"]
    return out
