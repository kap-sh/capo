"""Generated from Smithy shape ``com.amazonaws.appstream#EmbedHostDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.embed_host_domain

EmbedHostDomains: TypeAlias = list[
    "capo_appstream.types.embed_host_domain.EmbedHostDomain"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmbedHostDomains) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EmbedHostDomains:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EmbedHostDomains) -> list:
    return list(value)


def deserialize_cbor(data: list) -> EmbedHostDomains:
    return [item for item in data if item is not None]
