"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.eks_source
    import capo_resiliencehubv2.types.resource_tag_list
    import capo_resiliencehubv2.types.s3_url


class ResourceConfigurationResourceTagsMember(TypedDict, closed=True):
    resourceTags: "capo_resiliencehubv2.types.resource_tag_list.ResourceTagList"


class ResourceConfigurationCfnStackArnMember(TypedDict, closed=True):
    cfnStackArn: "capo_resiliencehubv2.types.arn.Arn"


class ResourceConfigurationTfStateFileUrlMember(TypedDict, closed=True):
    tfStateFileUrl: "capo_resiliencehubv2.types.s3_url.S3Url"


class ResourceConfigurationEksMember(TypedDict, closed=True):
    eks: "capo_resiliencehubv2.types.eks_source.EksSource"


class ResourceConfigurationDesignFileS3UrlMember(TypedDict, closed=True):
    designFileS3Url: "capo_resiliencehubv2.types.s3_url.S3Url"


ResourceConfiguration: TypeAlias = (
    ResourceConfigurationResourceTagsMember
    | ResourceConfigurationCfnStackArnMember
    | ResourceConfigurationTfStateFileUrlMember
    | ResourceConfigurationEksMember
    | ResourceConfigurationDesignFileS3UrlMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "resourceTags" in value:
        import capo_resiliencehubv2.types.resource_tag_list

        return {
            "resourceTags": capo_resiliencehubv2.types.resource_tag_list.serialize_json(
                value["resourceTags"]
            )
        }
    elif "cfnStackArn" in value:
        return {"cfnStackArn": value["cfnStackArn"]}
    elif "tfStateFileUrl" in value:
        return {"tfStateFileUrl": value["tfStateFileUrl"]}
    elif "eks" in value:
        import capo_resiliencehubv2.types.eks_source

        return {
            "eks": capo_resiliencehubv2.types.eks_source.serialize_json(value["eks"])
        }
    elif "designFileS3Url" in value:
        return {"designFileS3Url": value["designFileS3Url"]}
    else:
        raise SerializationError("ResourceConfiguration: no variant present")


def deserialize_json(data: dict) -> ResourceConfiguration:
    if data.get("resourceTags") is not None:
        import capo_resiliencehubv2.types.resource_tag_list

        return {
            "resourceTags": capo_resiliencehubv2.types.resource_tag_list.deserialize_json(
                data["resourceTags"]
            )
        }
    elif data.get("cfnStackArn") is not None:
        return {"cfnStackArn": data["cfnStackArn"]}
    elif data.get("tfStateFileUrl") is not None:
        return {"tfStateFileUrl": data["tfStateFileUrl"]}
    elif data.get("eks") is not None:
        import capo_resiliencehubv2.types.eks_source

        return {
            "eks": capo_resiliencehubv2.types.eks_source.deserialize_json(data["eks"])
        }
    elif data.get("designFileS3Url") is not None:
        return {"designFileS3Url": data["designFileS3Url"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceConfiguration: no recognized variant key")


def redact_sensitive(value: ResourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "eks" in value:
        import capo_resiliencehubv2.types.eks_source

        out["eks"] = capo_resiliencehubv2.types.eks_source.redact_sensitive(
            value["eks"]
        )
    return out
