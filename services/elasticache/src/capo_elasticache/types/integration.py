"""Generated from Smithy shape ``com.amazonaws.elasticache#Integration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integration_status
    import capo_elasticache.types.integration_type


class Integration(TypedDict, closed=True):
    integration_type: NotRequired[
        "capo_elasticache.types.integration_type.IntegrationType"
    ]
    """<p>The integration type. ElastiCache supports <code>dynamodb</code>.</p>"""
    status: NotRequired["capo_elasticache.types.integration_status.IntegrationStatus"]
    """<p>The current status of the integration. Valid values are:</p> <ul> <li> <p> <code>enabled</code> – The integration is enabled.</p> </li> <li> <p> <code>disabled</code> – The integration is disabled.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Integration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_type" in value:
        import capo_elasticache.types.integration_type

        capo_elasticache.types.integration_type.serialize_query(
            value["integration_type"], pairs, f"{key_prefix}IntegrationType"
        )
    if "status" in value:
        import capo_elasticache.types.integration_status

        capo_elasticache.types.integration_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_query(el: Element) -> Integration:
    out: Integration = {}  # type: ignore[typeddict-item]
    child_integration_type = el.find("IntegrationType")
    if child_integration_type is not None:
        import capo_elasticache.types.integration_type

        out["integration_type"] = (
            capo_elasticache.types.integration_type.deserialize_query(
                child_integration_type
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_elasticache.types.integration_status

        out["status"] = capo_elasticache.types.integration_status.deserialize_query(
            child_status
        )
    return out
