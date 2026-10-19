"""Generated from Smithy shape ``com.amazonaws.ecrpublic#Registry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.arn
    import capo_ecr_public.types.registry_alias_list
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.registry_verified
    import capo_ecr_public.types.url


class Registry(TypedDict, closed=True):
    registry_id: "capo_ecr_public.types.registry_id.RegistryId"
    """<p>The Amazon Web Services account ID that's associated with the registry. If you do not specify a registry, the default public registry is assumed.</p>"""
    registry_arn: "capo_ecr_public.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the public registry.</p>"""
    registry_uri: "capo_ecr_public.types.url.Url"
    """<p>The URI of a public registry. The URI contains a universal prefix and the registry alias.</p>"""
    verified: "capo_ecr_public.types.registry_verified.RegistryVerified"
    """<p>Indicates whether the account is a verified Amazon Web Services Marketplace vendor. If an account is verified, each public repository receives a verified account badge on the Amazon ECR Public Gallery.</p>"""
    aliases: "capo_ecr_public.types.registry_alias_list.RegistryAliasList"
    """<p>An array of objects that represents the aliases for a public registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Registry) -> dict:
    out: dict = {}
    out["registryId"] = value["registry_id"]
    out["registryArn"] = value["registry_arn"]
    out["registryUri"] = value["registry_uri"]
    out["verified"] = value["verified"]
    import capo_ecr_public.types.registry_alias_list

    out["aliases"] = capo_ecr_public.types.registry_alias_list.serialize_aws_json_1_1(
        value["aliases"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Registry:
    out: Registry = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    else:
        out["registry_id"] = ""
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        out["registry_arn"] = ""
    if data.get("registryUri") is not None:
        out["registry_uri"] = data["registryUri"]
    else:
        out["registry_uri"] = ""
    if data.get("verified") is not None:
        out["verified"] = data["verified"]
    else:
        out["verified"] = False
    if data.get("aliases") is not None:
        import capo_ecr_public.types.registry_alias_list

        out["aliases"] = (
            capo_ecr_public.types.registry_alias_list.deserialize_aws_json_1_1(
                data["aliases"]
            )
        )
    else:
        out["aliases"] = []
    return out
