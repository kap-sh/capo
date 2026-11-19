"""Generated from Smithy shape ``com.amazonaws.elasticache#IntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integration_type


class IntegrationRequest(TypedDict, closed=True):
    integration_type: NotRequired[
        "capo_elasticache.types.integration_type.IntegrationType"
    ]
    """<p>The integration type to enable. Must be <code>dynamodb</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_type" in value:
        import capo_elasticache.types.integration_type

        capo_elasticache.types.integration_type.serialize_query(
            value["integration_type"], pairs, f"{key_prefix}IntegrationType"
        )


def deserialize_query(el: Element) -> IntegrationRequest:
    out: IntegrationRequest = {}  # type: ignore[typeddict-item]
    child_integration_type = el.find("IntegrationType")
    if child_integration_type is not None:
        import capo_elasticache.types.integration_type

        out["integration_type"] = (
            capo_elasticache.types.integration_type.deserialize_query(
                child_integration_type
            )
        )
    return out
