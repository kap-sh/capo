"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositorySyncDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_sync_definition

RepositorySyncDefinitionList: TypeAlias = list[
    "capo_codeconnections.types.repository_sync_definition.RepositorySyncDefinition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinitionList) -> list:
    import capo_codeconnections.types.repository_sync_definition

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.repository_sync_definition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncDefinitionList:
    import capo_codeconnections.types.repository_sync_definition

    out: RepositorySyncDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codeconnections.types.repository_sync_definition.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RepositorySyncDefinitionList) -> list:
    import capo_codeconnections.types.repository_sync_definition

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.repository_sync_definition.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> RepositorySyncDefinitionList:
    import capo_codeconnections.types.repository_sync_definition

    out: RepositorySyncDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codeconnections.types.repository_sync_definition.deserialize_cbor(item)
        )
    return out
