"""Generated from Smithy shape ``com.amazonaws.elasticache#IntegrationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integration_request

IntegrationRequestList: TypeAlias = list[
    "capo_elasticache.types.integration_request.IntegrationRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.integration_request

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elasticache.types.integration_request.serialize_query(
            item, pairs, f"{prefix}.IntegrationRequest.{n}"
        )


def deserialize_query(el: Element) -> IntegrationRequestList:
    import capo_elasticache.types.integration_request

    out: IntegrationRequestList = []
    for child in el.findall("IntegrationRequest"):
        out.append(capo_elasticache.types.integration_request.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IntegrationRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.integration_request

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elasticache.types.integration_request.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> IntegrationRequestList:
    import capo_elasticache.types.integration_request

    out: IntegrationRequestList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.integration_request.deserialize_query(child))
    return out
