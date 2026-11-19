"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateOperationV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.enriched_properties
    import capo_mgn.types.operation_configuration_union
    import capo_mgn.types.properties_to_delete
    import capo_mgn.types.segment_construct_name


class UpdateOperationV2(TypedDict, closed=True):
    name: NotRequired["capo_mgn.types.segment_construct_name.SegmentConstructName"]
    """<p>The updated name for the construct.</p>"""
    excluded: NotRequired["bool"]
    """<p>Whether to exclude this construct from the migration.</p>"""
    properties: NotRequired["capo_mgn.types.enriched_properties.EnrichedProperties"]
    """<p>The properties to set or overwrite on the construct, using their native value types; omitted keys are unchanged.</p>"""
    properties_to_delete: NotRequired[
        "capo_mgn.types.properties_to_delete.PropertiesToDelete"
    ]
    """<p>The property keys to remove from the construct.</p>"""
    configuration: NotRequired[
        "capo_mgn.types.operation_configuration_union.OperationConfigurationUnion"
    ]
    """<p>Construct-type-specific behavioral configuration to apply, such as security group associations or security group rule referencing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOperationV2) -> dict:
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
    if "properties_to_delete" in value:
        import capo_mgn.types.properties_to_delete

        out["propertiesToDelete"] = capo_mgn.types.properties_to_delete.serialize_json(
            value["properties_to_delete"]
        )
    if "configuration" in value:
        import capo_mgn.types.operation_configuration_union

        out["configuration"] = (
            capo_mgn.types.operation_configuration_union.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOperationV2:
    out: UpdateOperationV2 = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("excluded") is not None:
        out["excluded"] = data["excluded"]
    if data.get("properties") is not None:
        import capo_mgn.types.enriched_properties

        out["properties"] = capo_mgn.types.enriched_properties.deserialize_json(
            data["properties"]
        )
    if data.get("propertiesToDelete") is not None:
        import capo_mgn.types.properties_to_delete

        out["properties_to_delete"] = (
            capo_mgn.types.properties_to_delete.deserialize_json(
                data["propertiesToDelete"]
            )
        )
    if data.get("configuration") is not None:
        import capo_mgn.types.operation_configuration_union

        out["configuration"] = (
            capo_mgn.types.operation_configuration_union.deserialize_json(
                data["configuration"]
            )
        )
    return out
