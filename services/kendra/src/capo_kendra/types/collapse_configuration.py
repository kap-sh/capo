"""Generated from Smithy shape ``com.amazonaws.kendra#CollapseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.document_attribute_key
    import capo_kendra.types.expand_configuration
    import capo_kendra.types.missing_attribute_key_strategy
    import capo_kendra.types.sorting_configuration_list


class CollapseConfiguration(TypedDict, closed=True):
    document_attribute_key: (
        "capo_kendra.types.document_attribute_key.DocumentAttributeKey"
    )
    """<p>The document attribute used to group search results. You can use any attribute that has the <code>Sortable</code> flag set to true. You can also sort by any of the following built-in attributes:"_category","_created_at", "_last_updated_at", "_version", "_view_count".</p>"""
    sorting_configurations: NotRequired[
        "capo_kendra.types.sorting_configuration_list.SortingConfigurationList"
    ]
    """<p>A prioritized list of document attributes/fields that determine the primary document among those in a collapsed group.</p>"""
    missing_attribute_key_strategy: NotRequired[
        "capo_kendra.types.missing_attribute_key_strategy.MissingAttributeKeyStrategy"
    ]
    """<p>Specifies the behavior for documents without a value for the collapse attribute.</p> <p>Amazon Kendra offers three customization options:</p> <ul> <li> <p>Choose to <code>COLLAPSE</code> all documents with null or missing values in one group. This is the default configuration.</p> </li> <li> <p>Choose to <code>IGNORE</code> documents with null or missing values. Ignored documents will not appear in query results.</p> </li> <li> <p>Choose to <code>EXPAND</code> each document with a null or missing value into a group of its own.</p> </li> </ul>"""
    expand: "capo_kendra.types.boolean.Boolean"
    """<p>Specifies whether to expand the collapsed results.</p>"""
    expand_configuration: NotRequired[
        "capo_kendra.types.expand_configuration.ExpandConfiguration"
    ]
    """<p>Provides configuration information to customize expansion options for a collapsed group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollapseConfiguration) -> dict:
    out: dict = {}
    out["DocumentAttributeKey"] = value["document_attribute_key"]
    if "sorting_configurations" in value:
        import capo_kendra.types.sorting_configuration_list

        out["SortingConfigurations"] = (
            capo_kendra.types.sorting_configuration_list.serialize_aws_json_1_1(
                value["sorting_configurations"]
            )
        )
    if "missing_attribute_key_strategy" in value:
        import capo_kendra.types.missing_attribute_key_strategy

        out["MissingAttributeKeyStrategy"] = (
            capo_kendra.types.missing_attribute_key_strategy.serialize_aws_json_1_1(
                value["missing_attribute_key_strategy"]
            )
        )
    out["Expand"] = value.get("expand", False)
    if "expand_configuration" in value:
        import capo_kendra.types.expand_configuration

        out["ExpandConfiguration"] = (
            capo_kendra.types.expand_configuration.serialize_aws_json_1_1(
                value["expand_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CollapseConfiguration:
    out: CollapseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DocumentAttributeKey") is not None:
        out["document_attribute_key"] = data["DocumentAttributeKey"]
    else:
        raise DeserializationError(
            "CollapseConfiguration.document_attribute_key required"
        )
    if data.get("SortingConfigurations") is not None:
        import capo_kendra.types.sorting_configuration_list

        out["sorting_configurations"] = (
            capo_kendra.types.sorting_configuration_list.deserialize_aws_json_1_1(
                data["SortingConfigurations"]
            )
        )
    if data.get("MissingAttributeKeyStrategy") is not None:
        import capo_kendra.types.missing_attribute_key_strategy

        out["missing_attribute_key_strategy"] = (
            capo_kendra.types.missing_attribute_key_strategy.deserialize_aws_json_1_1(
                data["MissingAttributeKeyStrategy"]
            )
        )
    if data.get("Expand") is not None:
        out["expand"] = data["Expand"]
    else:
        out["expand"] = False
    if data.get("ExpandConfiguration") is not None:
        import capo_kendra.types.expand_configuration

        out["expand_configuration"] = (
            capo_kendra.types.expand_configuration.deserialize_aws_json_1_1(
                data["ExpandConfiguration"]
            )
        )
    return out
