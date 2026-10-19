"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageSourceIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError, SerializationError
from capo_workspaces.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_workspaces.types.ec2_image_id
    import capo_workspaces.types.ec2_import_task_id
    import capo_workspaces.types.image_build_version_arn


class _ImageSourceIdentifier_Ec2ImportTaskId(TypedDict, closed=True):
    Ec2ImportTaskId: "capo_workspaces.types.ec2_import_task_id.Ec2ImportTaskId"


class _ImageSourceIdentifier_ImageBuildVersionArn(TypedDict, closed=True):
    ImageBuildVersionArn: (
        "capo_workspaces.types.image_build_version_arn.ImageBuildVersionArn"
    )


class _ImageSourceIdentifier_Ec2ImageId(TypedDict, closed=True):
    Ec2ImageId: "capo_workspaces.types.ec2_image_id.Ec2ImageId"


ImageSourceIdentifier: TypeAlias = (
    _ImageSourceIdentifier_Ec2ImportTaskId
    | _ImageSourceIdentifier_ImageBuildVersionArn
    | _ImageSourceIdentifier_Ec2ImageId
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageSourceIdentifier) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ImageSourceIdentifier: cannot serialize unknown variant {value.name!r}"
        )
    elif "Ec2ImportTaskId" in value:
        return {"Ec2ImportTaskId": value["Ec2ImportTaskId"]}
    elif "ImageBuildVersionArn" in value:
        return {"ImageBuildVersionArn": value["ImageBuildVersionArn"]}
    elif "Ec2ImageId" in value:
        return {"Ec2ImageId": value["Ec2ImageId"]}
    else:
        raise SerializationError("ImageSourceIdentifier: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ImageSourceIdentifier:
    if data.get("Ec2ImportTaskId") is not None:
        return {"Ec2ImportTaskId": data["Ec2ImportTaskId"]}
    elif data.get("ImageBuildVersionArn") is not None:
        return {"ImageBuildVersionArn": data["ImageBuildVersionArn"]}
    elif data.get("Ec2ImageId") is not None:
        return {"Ec2ImageId": data["Ec2ImageId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ImageSourceIdentifier: no recognized variant key")
