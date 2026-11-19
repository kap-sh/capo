"""Generated from Smithy shape ``com.amazonaws.cloudwatch#OTelEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudwatch._protocol.xml import Element

"""<p>The status of OTel enrichment for the account.</p>"""
OTelEnrichmentStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OTelEnrichmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OTelEnrichmentStatus:
    return cast(OTelEnrichmentStatus, data)


# --- awsQuery ser/de ---
def to_query_text(value: OTelEnrichmentStatus) -> str:
    return value


def from_query_text(text: str) -> OTelEnrichmentStatus:
    return cast(OTelEnrichmentStatus, text)


def serialize_query(
    value: OTelEnrichmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OTelEnrichmentStatus:
    return from_query_text(el.text or "")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OTelEnrichmentStatus) -> str:
    return value


def deserialize_cbor(data: str) -> OTelEnrichmentStatus:
    return cast(OTelEnrichmentStatus, data)
