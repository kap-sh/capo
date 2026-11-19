"""Generated from Smithy shape ``com.amazonaws.mgn#CreateOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.enriched_properties
    import capo_mgn.types.operation_configuration_union
    import capo_mgn.types.segment_construct_name


class CreateOperation(TypedDict, closed=True):
    name: NotRequired["capo_mgn.types.segment_construct_name.SegmentConstructName"]
    """<p>The name for the new construct.</p>"""
    excluded: NotRequired["bool"]
    """<p>Whether the new construct is excluded from the migration.</p>"""
    properties: NotRequired["capo_mgn.types.enriched_properties.EnrichedProperties"]
    """<p>The properties of the new construct, using their native value types.</p>"""
    configuration: NotRequired[
        "capo_mgn.types.operation_configuration_union.OperationConfigurationUnion"
    ]
    """<p>The initial construct-type-specific behavioral configuration for the new construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOperation) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "properties" in value:
        import capo_mgn.types.enriched_properties

        out["properties"] = capo_mgn.types.enriched_properties.serialize_json(
            value["properties"]
        )
    if "configuration" in value:
        import capo_mgn.types.operation_configuration_union

        out["configuration"] = (
            capo_mgn.types.operation_configuration_union.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateOperation:
    out: CreateOperation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("excluded") is not None:
        out["excluded"] = data["excluded"]
    if data.get("properties") is not None:
        import capo_mgn.types.enriched_properties

        out["properties"] = capo_mgn.types.enriched_properties.deserialize_json(
            data["properties"]
        )
    if data.get("configuration") is not None:
        import capo_mgn.types.operation_configuration_union

        out["configuration"] = (
            capo_mgn.types.operation_configuration_union.deserialize_json(
                data["configuration"]
            )
        )
    return out
