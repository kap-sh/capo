"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsLambdaFunctionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.architecture_list
    import capo_inspector2.types.execution_role_arn
    import capo_inspector2.types.function_name
    import capo_inspector2.types.lambda_vpc_config
    import capo_inspector2.types.layer_list
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.package_type
    import capo_inspector2.types.runtime
    import capo_inspector2.types.version


class AwsLambdaFunctionDetails(TypedDict, closed=True):
    function_name: "capo_inspector2.types.function_name.FunctionName"
    """<p>The name of the Amazon Web Services Lambda function.</p>"""
    runtime: "capo_inspector2.types.runtime.Runtime"
    """<p>The runtime environment for the Amazon Web Services Lambda function.</p>"""
    code_sha256: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The SHA256 hash of the Amazon Web Services Lambda function's deployment package.</p>"""
    version: "capo_inspector2.types.version.Version"
    """<p>The version of the Amazon Web Services Lambda function.</p>"""
    execution_role_arn: "capo_inspector2.types.execution_role_arn.ExecutionRoleArn"
    """<p>The Amazon Web Services Lambda function's execution role.</p>"""
    layers: NotRequired["capo_inspector2.types.layer_list.LayerList"]
    """<p>The Amazon Web Services Lambda function's <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html"> layers</a>. A Lambda function can have up to five layers.</p>"""
    vpc_config: NotRequired["capo_inspector2.types.lambda_vpc_config.LambdaVpcConfig"]
    """<p>The Amazon Web Services Lambda function's networking configuration.</p>"""
    package_type: NotRequired["capo_inspector2.types.package_type.PackageType"]
    """<p>The type of deployment package. Set to <code>Image</code> for container image and set <code>Zip</code> for .zip file archive.</p>"""
    architectures: NotRequired[
        "capo_inspector2.types.architecture_list.ArchitectureList"
    ]
    """<p>The instruction set architecture that the Amazon Web Services Lambda function supports. Architecture is a string array with one of the valid values. The default architecture value is <code>x86_64</code>.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The date and time that a user last updated the configuration, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601 format</a> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionDetails) -> dict:
    out: dict = {}
    out["functionName"] = value["function_name"]
    out["runtime"] = value["runtime"]
    out["codeSha256"] = value["code_sha256"]
    out["version"] = value["version"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "layers" in value:
        import capo_inspector2.types.layer_list

        out["layers"] = capo_inspector2.types.layer_list.serialize_json(value["layers"])
    if "vpc_config" in value:
        import capo_inspector2.types.lambda_vpc_config

        out["vpcConfig"] = capo_inspector2.types.lambda_vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "package_type" in value:
        out["packageType"] = value["package_type"]
    if "architectures" in value:
        import capo_inspector2.types.architecture_list

        out["architectures"] = capo_inspector2.types.architecture_list.serialize_json(
            value["architectures"]
        )
    if "last_modified_at" in value:
        import capo_inspector2.types._prelude.timestamp

        out["lastModifiedAt"] = capo_inspector2.types._prelude.timestamp.serialize_json(
            value["last_modified_at"]
        )
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionDetails:
    out: AwsLambdaFunctionDetails = {}  # type: ignore[typeddict-item]
    if data.get("functionName") is not None:
        out["function_name"] = data["functionName"]
    else:
        raise DeserializationError("AwsLambdaFunctionDetails.function_name required")
    if data.get("runtime") is not None:
        out["runtime"] = data["runtime"]
    else:
        raise DeserializationError("AwsLambdaFunctionDetails.runtime required")
    if data.get("codeSha256") is not None:
        out["code_sha256"] = data["codeSha256"]
    else:
        raise DeserializationError("AwsLambdaFunctionDetails.code_sha256 required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("AwsLambdaFunctionDetails.version required")
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "AwsLambdaFunctionDetails.execution_role_arn required"
        )
    if data.get("layers") is not None:
        import capo_inspector2.types.layer_list

        out["layers"] = capo_inspector2.types.layer_list.deserialize_json(
            data["layers"]
        )
    if data.get("vpcConfig") is not None:
        import capo_inspector2.types.lambda_vpc_config

        out["vpc_config"] = capo_inspector2.types.lambda_vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if data.get("packageType") is not None:
        out["package_type"] = data["packageType"]
    if data.get("architectures") is not None:
        import capo_inspector2.types.architecture_list

        out["architectures"] = capo_inspector2.types.architecture_list.deserialize_json(
            data["architectures"]
        )
    if data.get("lastModifiedAt") is not None:
        import capo_inspector2.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastModifiedAt"]
            )
        )
    return out
