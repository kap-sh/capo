"""Generated from Smithy shape ``com.amazonaws.firehose#OpenXJsonSerDe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.column_to_json_key_mappings


class OpenXJsonSerDe(TypedDict, closed=True):
    convert_dots_in_json_keys_to_underscores: NotRequired[
        "capo_firehose.types.boolean_object.BooleanObject"
    ]
    """<p>When set to <code>true</code>, specifies that the names of the keys include dots and that you want Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option.</p> <p>The default is <code>false</code>.</p>"""
    case_insensitive: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>When set to <code>true</code>, which is the default, Firehose converts JSON keys to lowercase before deserializing them.</p>"""
    column_to_json_key_mappings: NotRequired[
        "capo_firehose.types.column_to_json_key_mappings.ColumnToJsonKeyMappings"
    ]
    """<p>Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, <code>timestamp</code> is a Hive keyword. If you have a JSON key named <code>timestamp</code>, set this parameter to <code>{"ts": "timestamp"}</code> to map this key to a column named <code>ts</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenXJsonSerDe) -> dict:
    out: dict = {}
    if "convert_dots_in_json_keys_to_underscores" in value:
        out["ConvertDotsInJsonKeysToUnderscores"] = value[
            "convert_dots_in_json_keys_to_underscores"
        ]
    if "case_insensitive" in value:
        out["CaseInsensitive"] = value["case_insensitive"]
    if "column_to_json_key_mappings" in value:
        import capo_firehose.types.column_to_json_key_mappings

        out["ColumnToJsonKeyMappings"] = (
            capo_firehose.types.column_to_json_key_mappings.serialize_aws_json_1_1(
                value["column_to_json_key_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenXJsonSerDe:
    out: OpenXJsonSerDe = {}  # type: ignore[typeddict-item]
    if data.get("ConvertDotsInJsonKeysToUnderscores") is not None:
        out["convert_dots_in_json_keys_to_underscores"] = data[
            "ConvertDotsInJsonKeysToUnderscores"
        ]
    if data.get("CaseInsensitive") is not None:
        out["case_insensitive"] = data["CaseInsensitive"]
    if data.get("ColumnToJsonKeyMappings") is not None:
        import capo_firehose.types.column_to_json_key_mappings

        out["column_to_json_key_mappings"] = (
            capo_firehose.types.column_to_json_key_mappings.deserialize_aws_json_1_1(
                data["ColumnToJsonKeyMappings"]
            )
        )
    return out
