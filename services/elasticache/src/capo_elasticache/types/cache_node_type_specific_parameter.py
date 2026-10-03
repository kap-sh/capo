"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeTypeSpecificParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.cache_node_type_specific_value_list
    import capo_elasticache.types.change_type
    import capo_elasticache.types.string


class CacheNodeTypeSpecificParameter(TypedDict, closed=True):
    parameter_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the parameter.</p>"""
    description: NotRequired["capo_elasticache.types.string.String"]
    """<p>A description of the parameter.</p>"""
    source: NotRequired["capo_elasticache.types.string.String"]
    """<p>The source of the parameter value.</p>"""
    data_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The valid data type for the parameter.</p>"""
    allowed_values: NotRequired["capo_elasticache.types.string.String"]
    """<p>The valid range of values for the parameter.</p>"""
    is_modifiable: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>Indicates whether (<code>true</code>) or not (<code>false</code>) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.</p>"""
    minimum_engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The earliest cache engine version to which the parameter can apply.</p>"""
    cache_node_type_specific_values: NotRequired[
        "capo_elasticache.types.cache_node_type_specific_value_list.CacheNodeTypeSpecificValueList"
    ]
    """<p>A list of cache node types and their corresponding values for this parameter.</p>"""
    change_type: NotRequired["capo_elasticache.types.change_type.ChangeType"]
    """<p>Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see <a href="https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Clusters.Rebooting.html">Rebooting a Cluster</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeTypeSpecificParameter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_name" in value:
        pairs.append((f"{key_prefix}ParameterName", str(value["parameter_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "data_type" in value:
        pairs.append((f"{key_prefix}DataType", str(value["data_type"])))
    if "allowed_values" in value:
        pairs.append((f"{key_prefix}AllowedValues", str(value["allowed_values"])))
    if "is_modifiable" in value:
        pairs.append(
            (f"{key_prefix}IsModifiable", "true" if value["is_modifiable"] else "false")
        )
    if "minimum_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MinimumEngineVersion", str(value["minimum_engine_version"]))
        )
    if "cache_node_type_specific_values" in value:
        import capo_elasticache.types.cache_node_type_specific_value_list

        capo_elasticache.types.cache_node_type_specific_value_list.serialize_query(
            value["cache_node_type_specific_values"],
            pairs,
            f"{key_prefix}CacheNodeTypeSpecificValues",
        )
    if "change_type" in value:
        import capo_elasticache.types.change_type

        capo_elasticache.types.change_type.serialize_query(
            value["change_type"], pairs, f"{key_prefix}ChangeType"
        )


def deserialize_query(el: Element) -> CacheNodeTypeSpecificParameter:
    out: CacheNodeTypeSpecificParameter = {}  # type: ignore[typeddict-item]
    child_parameter_name = el.find("ParameterName")
    if child_parameter_name is not None:
        out["parameter_name"] = str(child_parameter_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_data_type = el.find("DataType")
    if child_data_type is not None:
        out["data_type"] = str(child_data_type.text or "")
    child_allowed_values = el.find("AllowedValues")
    if child_allowed_values is not None:
        out["allowed_values"] = str(child_allowed_values.text or "")
    child_is_modifiable = el.find("IsModifiable")
    if child_is_modifiable is not None:
        out["is_modifiable"] = (child_is_modifiable.text or "").lower() == "true"
    child_minimum_engine_version = el.find("MinimumEngineVersion")
    if child_minimum_engine_version is not None:
        out["minimum_engine_version"] = str(child_minimum_engine_version.text or "")
    child_cache_node_type_specific_values = el.find("CacheNodeTypeSpecificValues")
    if child_cache_node_type_specific_values is not None:
        import capo_elasticache.types.cache_node_type_specific_value_list

        out["cache_node_type_specific_values"] = (
            capo_elasticache.types.cache_node_type_specific_value_list.deserialize_query(
                child_cache_node_type_specific_values
            )
        )
    child_change_type = el.find("ChangeType")
    if child_change_type is not None:
        import capo_elasticache.types.change_type

        out["change_type"] = capo_elasticache.types.change_type.deserialize_query(
            child_change_type
        )
    return out
