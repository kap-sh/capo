"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.account_aggregation
    import capo_inspector2.types.ami_aggregation
    import capo_inspector2.types.aws_ecr_container_aggregation
    import capo_inspector2.types.code_repository_aggregation
    import capo_inspector2.types.container_image_aggregation
    import capo_inspector2.types.ec2_instance_aggregation
    import capo_inspector2.types.finding_type_aggregation
    import capo_inspector2.types.image_layer_aggregation
    import capo_inspector2.types.lambda_function_aggregation
    import capo_inspector2.types.lambda_layer_aggregation
    import capo_inspector2.types.package_aggregation
    import capo_inspector2.types.repository_aggregation
    import capo_inspector2.types.serverless_function_aggregation
    import capo_inspector2.types.title_aggregation
    import capo_inspector2.types.vm_instance_aggregation


class _AggregationRequest_accountAggregation(TypedDict, closed=True):
    accountAggregation: "capo_inspector2.types.account_aggregation.AccountAggregation"


class _AggregationRequest_amiAggregation(TypedDict, closed=True):
    amiAggregation: "capo_inspector2.types.ami_aggregation.AmiAggregation"


class _AggregationRequest_awsEcrContainerAggregation(TypedDict, closed=True):
    awsEcrContainerAggregation: (
        "capo_inspector2.types.aws_ecr_container_aggregation.AwsEcrContainerAggregation"
    )


class _AggregationRequest_ec2InstanceAggregation(TypedDict, closed=True):
    ec2InstanceAggregation: (
        "capo_inspector2.types.ec2_instance_aggregation.Ec2InstanceAggregation"
    )


class _AggregationRequest_findingTypeAggregation(TypedDict, closed=True):
    findingTypeAggregation: (
        "capo_inspector2.types.finding_type_aggregation.FindingTypeAggregation"
    )


class _AggregationRequest_imageLayerAggregation(TypedDict, closed=True):
    imageLayerAggregation: (
        "capo_inspector2.types.image_layer_aggregation.ImageLayerAggregation"
    )


class _AggregationRequest_packageAggregation(TypedDict, closed=True):
    packageAggregation: "capo_inspector2.types.package_aggregation.PackageAggregation"


class _AggregationRequest_repositoryAggregation(TypedDict, closed=True):
    repositoryAggregation: (
        "capo_inspector2.types.repository_aggregation.RepositoryAggregation"
    )


class _AggregationRequest_titleAggregation(TypedDict, closed=True):
    titleAggregation: "capo_inspector2.types.title_aggregation.TitleAggregation"


class _AggregationRequest_lambdaLayerAggregation(TypedDict, closed=True):
    lambdaLayerAggregation: (
        "capo_inspector2.types.lambda_layer_aggregation.LambdaLayerAggregation"
    )


class _AggregationRequest_lambdaFunctionAggregation(TypedDict, closed=True):
    lambdaFunctionAggregation: (
        "capo_inspector2.types.lambda_function_aggregation.LambdaFunctionAggregation"
    )


class _AggregationRequest_codeRepositoryAggregation(TypedDict, closed=True):
    codeRepositoryAggregation: (
        "capo_inspector2.types.code_repository_aggregation.CodeRepositoryAggregation"
    )


class _AggregationRequest_vmInstanceAggregation(TypedDict, closed=True):
    vmInstanceAggregation: (
        "capo_inspector2.types.vm_instance_aggregation.VmInstanceAggregation"
    )


class _AggregationRequest_containerImageAggregation(TypedDict, closed=True):
    containerImageAggregation: (
        "capo_inspector2.types.container_image_aggregation.ContainerImageAggregation"
    )


class _AggregationRequest_serverlessFunctionAggregation(TypedDict, closed=True):
    serverlessFunctionAggregation: "capo_inspector2.types.serverless_function_aggregation.ServerlessFunctionAggregation"


AggregationRequest: TypeAlias = (
    _AggregationRequest_accountAggregation
    | _AggregationRequest_amiAggregation
    | _AggregationRequest_awsEcrContainerAggregation
    | _AggregationRequest_ec2InstanceAggregation
    | _AggregationRequest_findingTypeAggregation
    | _AggregationRequest_imageLayerAggregation
    | _AggregationRequest_packageAggregation
    | _AggregationRequest_repositoryAggregation
    | _AggregationRequest_titleAggregation
    | _AggregationRequest_lambdaLayerAggregation
    | _AggregationRequest_lambdaFunctionAggregation
    | _AggregationRequest_codeRepositoryAggregation
    | _AggregationRequest_vmInstanceAggregation
    | _AggregationRequest_containerImageAggregation
    | _AggregationRequest_serverlessFunctionAggregation
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AggregationRequest) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AggregationRequest: cannot serialize unknown variant {value.name!r}"
        )
    elif "accountAggregation" in value:
        import capo_inspector2.types.account_aggregation

        return {
            "accountAggregation": capo_inspector2.types.account_aggregation.serialize_json(
                value["accountAggregation"]
            )
        }
    elif "amiAggregation" in value:
        import capo_inspector2.types.ami_aggregation

        return {
            "amiAggregation": capo_inspector2.types.ami_aggregation.serialize_json(
                value["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in value:
        import capo_inspector2.types.aws_ecr_container_aggregation

        return {
            "awsEcrContainerAggregation": capo_inspector2.types.aws_ecr_container_aggregation.serialize_json(
                value["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in value:
        import capo_inspector2.types.ec2_instance_aggregation

        return {
            "ec2InstanceAggregation": capo_inspector2.types.ec2_instance_aggregation.serialize_json(
                value["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in value:
        import capo_inspector2.types.finding_type_aggregation

        return {
            "findingTypeAggregation": capo_inspector2.types.finding_type_aggregation.serialize_json(
                value["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in value:
        import capo_inspector2.types.image_layer_aggregation

        return {
            "imageLayerAggregation": capo_inspector2.types.image_layer_aggregation.serialize_json(
                value["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in value:
        import capo_inspector2.types.package_aggregation

        return {
            "packageAggregation": capo_inspector2.types.package_aggregation.serialize_json(
                value["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in value:
        import capo_inspector2.types.repository_aggregation

        return {
            "repositoryAggregation": capo_inspector2.types.repository_aggregation.serialize_json(
                value["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in value:
        import capo_inspector2.types.title_aggregation

        return {
            "titleAggregation": capo_inspector2.types.title_aggregation.serialize_json(
                value["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in value:
        import capo_inspector2.types.lambda_layer_aggregation

        return {
            "lambdaLayerAggregation": capo_inspector2.types.lambda_layer_aggregation.serialize_json(
                value["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in value:
        import capo_inspector2.types.lambda_function_aggregation

        return {
            "lambdaFunctionAggregation": capo_inspector2.types.lambda_function_aggregation.serialize_json(
                value["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in value:
        import capo_inspector2.types.code_repository_aggregation

        return {
            "codeRepositoryAggregation": capo_inspector2.types.code_repository_aggregation.serialize_json(
                value["codeRepositoryAggregation"]
            )
        }
    elif "vmInstanceAggregation" in value:
        import capo_inspector2.types.vm_instance_aggregation

        return {
            "vmInstanceAggregation": capo_inspector2.types.vm_instance_aggregation.serialize_json(
                value["vmInstanceAggregation"]
            )
        }
    elif "containerImageAggregation" in value:
        import capo_inspector2.types.container_image_aggregation

        return {
            "containerImageAggregation": capo_inspector2.types.container_image_aggregation.serialize_json(
                value["containerImageAggregation"]
            )
        }
    elif "serverlessFunctionAggregation" in value:
        import capo_inspector2.types.serverless_function_aggregation

        return {
            "serverlessFunctionAggregation": capo_inspector2.types.serverless_function_aggregation.serialize_json(
                value["serverlessFunctionAggregation"]
            )
        }
    else:
        raise SerializationError("AggregationRequest: no variant present")


def deserialize_json(data: dict) -> AggregationRequest:
    if data.get("accountAggregation") is not None:
        import capo_inspector2.types.account_aggregation

        return {
            "accountAggregation": capo_inspector2.types.account_aggregation.deserialize_json(
                data["accountAggregation"]
            )
        }
    elif data.get("amiAggregation") is not None:
        import capo_inspector2.types.ami_aggregation

        return {
            "amiAggregation": capo_inspector2.types.ami_aggregation.deserialize_json(
                data["amiAggregation"]
            )
        }
    elif data.get("awsEcrContainerAggregation") is not None:
        import capo_inspector2.types.aws_ecr_container_aggregation

        return {
            "awsEcrContainerAggregation": capo_inspector2.types.aws_ecr_container_aggregation.deserialize_json(
                data["awsEcrContainerAggregation"]
            )
        }
    elif data.get("ec2InstanceAggregation") is not None:
        import capo_inspector2.types.ec2_instance_aggregation

        return {
            "ec2InstanceAggregation": capo_inspector2.types.ec2_instance_aggregation.deserialize_json(
                data["ec2InstanceAggregation"]
            )
        }
    elif data.get("findingTypeAggregation") is not None:
        import capo_inspector2.types.finding_type_aggregation

        return {
            "findingTypeAggregation": capo_inspector2.types.finding_type_aggregation.deserialize_json(
                data["findingTypeAggregation"]
            )
        }
    elif data.get("imageLayerAggregation") is not None:
        import capo_inspector2.types.image_layer_aggregation

        return {
            "imageLayerAggregation": capo_inspector2.types.image_layer_aggregation.deserialize_json(
                data["imageLayerAggregation"]
            )
        }
    elif data.get("packageAggregation") is not None:
        import capo_inspector2.types.package_aggregation

        return {
            "packageAggregation": capo_inspector2.types.package_aggregation.deserialize_json(
                data["packageAggregation"]
            )
        }
    elif data.get("repositoryAggregation") is not None:
        import capo_inspector2.types.repository_aggregation

        return {
            "repositoryAggregation": capo_inspector2.types.repository_aggregation.deserialize_json(
                data["repositoryAggregation"]
            )
        }
    elif data.get("titleAggregation") is not None:
        import capo_inspector2.types.title_aggregation

        return {
            "titleAggregation": capo_inspector2.types.title_aggregation.deserialize_json(
                data["titleAggregation"]
            )
        }
    elif data.get("lambdaLayerAggregation") is not None:
        import capo_inspector2.types.lambda_layer_aggregation

        return {
            "lambdaLayerAggregation": capo_inspector2.types.lambda_layer_aggregation.deserialize_json(
                data["lambdaLayerAggregation"]
            )
        }
    elif data.get("lambdaFunctionAggregation") is not None:
        import capo_inspector2.types.lambda_function_aggregation

        return {
            "lambdaFunctionAggregation": capo_inspector2.types.lambda_function_aggregation.deserialize_json(
                data["lambdaFunctionAggregation"]
            )
        }
    elif data.get("codeRepositoryAggregation") is not None:
        import capo_inspector2.types.code_repository_aggregation

        return {
            "codeRepositoryAggregation": capo_inspector2.types.code_repository_aggregation.deserialize_json(
                data["codeRepositoryAggregation"]
            )
        }
    elif data.get("vmInstanceAggregation") is not None:
        import capo_inspector2.types.vm_instance_aggregation

        return {
            "vmInstanceAggregation": capo_inspector2.types.vm_instance_aggregation.deserialize_json(
                data["vmInstanceAggregation"]
            )
        }
    elif data.get("containerImageAggregation") is not None:
        import capo_inspector2.types.container_image_aggregation

        return {
            "containerImageAggregation": capo_inspector2.types.container_image_aggregation.deserialize_json(
                data["containerImageAggregation"]
            )
        }
    elif data.get("serverlessFunctionAggregation") is not None:
        import capo_inspector2.types.serverless_function_aggregation

        return {
            "serverlessFunctionAggregation": capo_inspector2.types.serverless_function_aggregation.deserialize_json(
                data["serverlessFunctionAggregation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AggregationRequest: no recognized variant key")
