"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.account_aggregation_response
    import capo_inspector2.types.ami_aggregation_response
    import capo_inspector2.types.aws_ecr_container_aggregation_response
    import capo_inspector2.types.code_repository_aggregation_response
    import capo_inspector2.types.container_image_aggregation_response
    import capo_inspector2.types.ec2_instance_aggregation_response
    import capo_inspector2.types.finding_type_aggregation_response
    import capo_inspector2.types.image_layer_aggregation_response
    import capo_inspector2.types.lambda_function_aggregation_response
    import capo_inspector2.types.lambda_layer_aggregation_response
    import capo_inspector2.types.package_aggregation_response
    import capo_inspector2.types.repository_aggregation_response
    import capo_inspector2.types.serverless_function_aggregation_response
    import capo_inspector2.types.title_aggregation_response
    import capo_inspector2.types.vm_instance_aggregation_response


class _AggregationResponse_accountAggregation(TypedDict, closed=True):
    accountAggregation: (
        "capo_inspector2.types.account_aggregation_response.AccountAggregationResponse"
    )


class _AggregationResponse_amiAggregation(TypedDict, closed=True):
    amiAggregation: (
        "capo_inspector2.types.ami_aggregation_response.AmiAggregationResponse"
    )


class _AggregationResponse_awsEcrContainerAggregation(TypedDict, closed=True):
    awsEcrContainerAggregation: "capo_inspector2.types.aws_ecr_container_aggregation_response.AwsEcrContainerAggregationResponse"


class _AggregationResponse_ec2InstanceAggregation(TypedDict, closed=True):
    ec2InstanceAggregation: "capo_inspector2.types.ec2_instance_aggregation_response.Ec2InstanceAggregationResponse"


class _AggregationResponse_findingTypeAggregation(TypedDict, closed=True):
    findingTypeAggregation: "capo_inspector2.types.finding_type_aggregation_response.FindingTypeAggregationResponse"


class _AggregationResponse_imageLayerAggregation(TypedDict, closed=True):
    imageLayerAggregation: "capo_inspector2.types.image_layer_aggregation_response.ImageLayerAggregationResponse"


class _AggregationResponse_packageAggregation(TypedDict, closed=True):
    packageAggregation: (
        "capo_inspector2.types.package_aggregation_response.PackageAggregationResponse"
    )


class _AggregationResponse_repositoryAggregation(TypedDict, closed=True):
    repositoryAggregation: "capo_inspector2.types.repository_aggregation_response.RepositoryAggregationResponse"


class _AggregationResponse_titleAggregation(TypedDict, closed=True):
    titleAggregation: (
        "capo_inspector2.types.title_aggregation_response.TitleAggregationResponse"
    )


class _AggregationResponse_lambdaLayerAggregation(TypedDict, closed=True):
    lambdaLayerAggregation: "capo_inspector2.types.lambda_layer_aggregation_response.LambdaLayerAggregationResponse"


class _AggregationResponse_lambdaFunctionAggregation(TypedDict, closed=True):
    lambdaFunctionAggregation: "capo_inspector2.types.lambda_function_aggregation_response.LambdaFunctionAggregationResponse"


class _AggregationResponse_codeRepositoryAggregation(TypedDict, closed=True):
    codeRepositoryAggregation: "capo_inspector2.types.code_repository_aggregation_response.CodeRepositoryAggregationResponse"


class _AggregationResponse_vmInstanceAggregation(TypedDict, closed=True):
    vmInstanceAggregation: "capo_inspector2.types.vm_instance_aggregation_response.VmInstanceAggregationResponse"


class _AggregationResponse_containerImageAggregation(TypedDict, closed=True):
    containerImageAggregation: "capo_inspector2.types.container_image_aggregation_response.ContainerImageAggregationResponse"


class _AggregationResponse_serverlessFunctionAggregation(TypedDict, closed=True):
    serverlessFunctionAggregation: "capo_inspector2.types.serverless_function_aggregation_response.ServerlessFunctionAggregationResponse"


AggregationResponse: TypeAlias = (
    _AggregationResponse_accountAggregation
    | _AggregationResponse_amiAggregation
    | _AggregationResponse_awsEcrContainerAggregation
    | _AggregationResponse_ec2InstanceAggregation
    | _AggregationResponse_findingTypeAggregation
    | _AggregationResponse_imageLayerAggregation
    | _AggregationResponse_packageAggregation
    | _AggregationResponse_repositoryAggregation
    | _AggregationResponse_titleAggregation
    | _AggregationResponse_lambdaLayerAggregation
    | _AggregationResponse_lambdaFunctionAggregation
    | _AggregationResponse_codeRepositoryAggregation
    | _AggregationResponse_vmInstanceAggregation
    | _AggregationResponse_containerImageAggregation
    | _AggregationResponse_serverlessFunctionAggregation
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AggregationResponse) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AggregationResponse: cannot serialize unknown variant {value.name!r}"
        )
    elif "accountAggregation" in value:
        import capo_inspector2.types.account_aggregation_response

        return {
            "accountAggregation": capo_inspector2.types.account_aggregation_response.serialize_json(
                value["accountAggregation"]
            )
        }
    elif "amiAggregation" in value:
        import capo_inspector2.types.ami_aggregation_response

        return {
            "amiAggregation": capo_inspector2.types.ami_aggregation_response.serialize_json(
                value["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in value:
        import capo_inspector2.types.aws_ecr_container_aggregation_response

        return {
            "awsEcrContainerAggregation": capo_inspector2.types.aws_ecr_container_aggregation_response.serialize_json(
                value["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in value:
        import capo_inspector2.types.ec2_instance_aggregation_response

        return {
            "ec2InstanceAggregation": capo_inspector2.types.ec2_instance_aggregation_response.serialize_json(
                value["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in value:
        import capo_inspector2.types.finding_type_aggregation_response

        return {
            "findingTypeAggregation": capo_inspector2.types.finding_type_aggregation_response.serialize_json(
                value["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in value:
        import capo_inspector2.types.image_layer_aggregation_response

        return {
            "imageLayerAggregation": capo_inspector2.types.image_layer_aggregation_response.serialize_json(
                value["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in value:
        import capo_inspector2.types.package_aggregation_response

        return {
            "packageAggregation": capo_inspector2.types.package_aggregation_response.serialize_json(
                value["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in value:
        import capo_inspector2.types.repository_aggregation_response

        return {
            "repositoryAggregation": capo_inspector2.types.repository_aggregation_response.serialize_json(
                value["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in value:
        import capo_inspector2.types.title_aggregation_response

        return {
            "titleAggregation": capo_inspector2.types.title_aggregation_response.serialize_json(
                value["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in value:
        import capo_inspector2.types.lambda_layer_aggregation_response

        return {
            "lambdaLayerAggregation": capo_inspector2.types.lambda_layer_aggregation_response.serialize_json(
                value["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in value:
        import capo_inspector2.types.lambda_function_aggregation_response

        return {
            "lambdaFunctionAggregation": capo_inspector2.types.lambda_function_aggregation_response.serialize_json(
                value["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in value:
        import capo_inspector2.types.code_repository_aggregation_response

        return {
            "codeRepositoryAggregation": capo_inspector2.types.code_repository_aggregation_response.serialize_json(
                value["codeRepositoryAggregation"]
            )
        }
    elif "vmInstanceAggregation" in value:
        import capo_inspector2.types.vm_instance_aggregation_response

        return {
            "vmInstanceAggregation": capo_inspector2.types.vm_instance_aggregation_response.serialize_json(
                value["vmInstanceAggregation"]
            )
        }
    elif "containerImageAggregation" in value:
        import capo_inspector2.types.container_image_aggregation_response

        return {
            "containerImageAggregation": capo_inspector2.types.container_image_aggregation_response.serialize_json(
                value["containerImageAggregation"]
            )
        }
    elif "serverlessFunctionAggregation" in value:
        import capo_inspector2.types.serverless_function_aggregation_response

        return {
            "serverlessFunctionAggregation": capo_inspector2.types.serverless_function_aggregation_response.serialize_json(
                value["serverlessFunctionAggregation"]
            )
        }
    else:
        raise SerializationError("AggregationResponse: no variant present")


def deserialize_json(data: dict) -> AggregationResponse:
    if data.get("accountAggregation") is not None:
        import capo_inspector2.types.account_aggregation_response

        return {
            "accountAggregation": capo_inspector2.types.account_aggregation_response.deserialize_json(
                data["accountAggregation"]
            )
        }
    elif data.get("amiAggregation") is not None:
        import capo_inspector2.types.ami_aggregation_response

        return {
            "amiAggregation": capo_inspector2.types.ami_aggregation_response.deserialize_json(
                data["amiAggregation"]
            )
        }
    elif data.get("awsEcrContainerAggregation") is not None:
        import capo_inspector2.types.aws_ecr_container_aggregation_response

        return {
            "awsEcrContainerAggregation": capo_inspector2.types.aws_ecr_container_aggregation_response.deserialize_json(
                data["awsEcrContainerAggregation"]
            )
        }
    elif data.get("ec2InstanceAggregation") is not None:
        import capo_inspector2.types.ec2_instance_aggregation_response

        return {
            "ec2InstanceAggregation": capo_inspector2.types.ec2_instance_aggregation_response.deserialize_json(
                data["ec2InstanceAggregation"]
            )
        }
    elif data.get("findingTypeAggregation") is not None:
        import capo_inspector2.types.finding_type_aggregation_response

        return {
            "findingTypeAggregation": capo_inspector2.types.finding_type_aggregation_response.deserialize_json(
                data["findingTypeAggregation"]
            )
        }
    elif data.get("imageLayerAggregation") is not None:
        import capo_inspector2.types.image_layer_aggregation_response

        return {
            "imageLayerAggregation": capo_inspector2.types.image_layer_aggregation_response.deserialize_json(
                data["imageLayerAggregation"]
            )
        }
    elif data.get("packageAggregation") is not None:
        import capo_inspector2.types.package_aggregation_response

        return {
            "packageAggregation": capo_inspector2.types.package_aggregation_response.deserialize_json(
                data["packageAggregation"]
            )
        }
    elif data.get("repositoryAggregation") is not None:
        import capo_inspector2.types.repository_aggregation_response

        return {
            "repositoryAggregation": capo_inspector2.types.repository_aggregation_response.deserialize_json(
                data["repositoryAggregation"]
            )
        }
    elif data.get("titleAggregation") is not None:
        import capo_inspector2.types.title_aggregation_response

        return {
            "titleAggregation": capo_inspector2.types.title_aggregation_response.deserialize_json(
                data["titleAggregation"]
            )
        }
    elif data.get("lambdaLayerAggregation") is not None:
        import capo_inspector2.types.lambda_layer_aggregation_response

        return {
            "lambdaLayerAggregation": capo_inspector2.types.lambda_layer_aggregation_response.deserialize_json(
                data["lambdaLayerAggregation"]
            )
        }
    elif data.get("lambdaFunctionAggregation") is not None:
        import capo_inspector2.types.lambda_function_aggregation_response

        return {
            "lambdaFunctionAggregation": capo_inspector2.types.lambda_function_aggregation_response.deserialize_json(
                data["lambdaFunctionAggregation"]
            )
        }
    elif data.get("codeRepositoryAggregation") is not None:
        import capo_inspector2.types.code_repository_aggregation_response

        return {
            "codeRepositoryAggregation": capo_inspector2.types.code_repository_aggregation_response.deserialize_json(
                data["codeRepositoryAggregation"]
            )
        }
    elif data.get("vmInstanceAggregation") is not None:
        import capo_inspector2.types.vm_instance_aggregation_response

        return {
            "vmInstanceAggregation": capo_inspector2.types.vm_instance_aggregation_response.deserialize_json(
                data["vmInstanceAggregation"]
            )
        }
    elif data.get("containerImageAggregation") is not None:
        import capo_inspector2.types.container_image_aggregation_response

        return {
            "containerImageAggregation": capo_inspector2.types.container_image_aggregation_response.deserialize_json(
                data["containerImageAggregation"]
            )
        }
    elif data.get("serverlessFunctionAggregation") is not None:
        import capo_inspector2.types.serverless_function_aggregation_response

        return {
            "serverlessFunctionAggregation": capo_inspector2.types.serverless_function_aggregation_response.deserialize_json(
                data["serverlessFunctionAggregation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AggregationResponse: no recognized variant key")
