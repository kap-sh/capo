"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.aws_ecs_metadata_details
    import capo_inspector2.types.aws_eks_metadata_details


class ClusterMetadataAwsEcsMetadataDetailsMember(TypedDict, closed=True):
    awsEcsMetadataDetails: (
        "capo_inspector2.types.aws_ecs_metadata_details.AwsEcsMetadataDetails"
    )


class ClusterMetadataAwsEksMetadataDetailsMember(TypedDict, closed=True):
    awsEksMetadataDetails: (
        "capo_inspector2.types.aws_eks_metadata_details.AwsEksMetadataDetails"
    )


ClusterMetadata: TypeAlias = (
    ClusterMetadataAwsEcsMetadataDetailsMember
    | ClusterMetadataAwsEksMetadataDetailsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ClusterMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ClusterMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "awsEcsMetadataDetails" in value:
        import capo_inspector2.types.aws_ecs_metadata_details

        return {
            "awsEcsMetadataDetails": capo_inspector2.types.aws_ecs_metadata_details.serialize_json(
                value["awsEcsMetadataDetails"]
            )
        }
    elif "awsEksMetadataDetails" in value:
        import capo_inspector2.types.aws_eks_metadata_details

        return {
            "awsEksMetadataDetails": capo_inspector2.types.aws_eks_metadata_details.serialize_json(
                value["awsEksMetadataDetails"]
            )
        }
    else:
        raise SerializationError("ClusterMetadata: no variant present")


def deserialize_json(data: dict) -> ClusterMetadata:
    if data.get("awsEcsMetadataDetails") is not None:
        import capo_inspector2.types.aws_ecs_metadata_details

        return {
            "awsEcsMetadataDetails": capo_inspector2.types.aws_ecs_metadata_details.deserialize_json(
                data["awsEcsMetadataDetails"]
            )
        }
    elif data.get("awsEksMetadataDetails") is not None:
        import capo_inspector2.types.aws_eks_metadata_details

        return {
            "awsEksMetadataDetails": capo_inspector2.types.aws_eks_metadata_details.deserialize_json(
                data["awsEksMetadataDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ClusterMetadata: no recognized variant key")
