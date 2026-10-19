"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryAlias``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.default_registry_alias_flag
    import capo_ecr_public.types.primary_registry_alias_flag
    import capo_ecr_public.types.registry_alias_name
    import capo_ecr_public.types.registry_alias_status


class RegistryAlias(TypedDict, closed=True):
    name: "capo_ecr_public.types.registry_alias_name.RegistryAliasName"
    """<p>The name of the registry alias.</p>"""
    status: "capo_ecr_public.types.registry_alias_status.RegistryAliasStatus"
    """<p>The status of the registry alias.</p>"""
    primary_registry_alias: (
        "capo_ecr_public.types.primary_registry_alias_flag.PrimaryRegistryAliasFlag"
    )
    """<p>Indicates whether the registry alias is the primary alias for the registry. If true, the alias is the primary registry alias and is displayed in both the repository URL and the image URI used in the <code>docker pull</code> commands on the Amazon ECR Public Gallery.</p> <note> <p>A registry alias that isn't the primary registry alias can be used in the repository URI in a <code>docker pull</code> command.</p> </note>"""
    default_registry_alias: (
        "capo_ecr_public.types.default_registry_alias_flag.DefaultRegistryAliasFlag"
    )
    """<p>Indicates whether the registry alias is the default alias for the registry. When the first public repository is created, your public registry is assigned a default registry alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryAlias) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_ecr_public.types.registry_alias_status

    out["status"] = capo_ecr_public.types.registry_alias_status.serialize_aws_json_1_1(
        value["status"]
    )
    out["primaryRegistryAlias"] = value.get("primary_registry_alias", False)
    out["defaultRegistryAlias"] = value.get("default_registry_alias", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryAlias:
    out: RegistryAlias = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_ecr_public.types.registry_alias_status

        out["status"] = (
            capo_ecr_public.types.registry_alias_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_ecr_public.types.registry_alias_status.RegistryAliasStatus", ""
        )
    if data.get("primaryRegistryAlias") is not None:
        out["primary_registry_alias"] = data["primaryRegistryAlias"]
    else:
        out["primary_registry_alias"] = False
    if data.get("defaultRegistryAlias") is not None:
        out["default_registry_alias"] = data["defaultRegistryAlias"]
    else:
        out["default_registry_alias"] = False
    return out
