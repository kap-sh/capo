"""Generated from Smithy shape ``com.amazonaws.cloudsearch#IndexField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.date_array_options
    import capo_cloudsearch.types.date_options
    import capo_cloudsearch.types.double_array_options
    import capo_cloudsearch.types.double_options
    import capo_cloudsearch.types.dynamic_field_name
    import capo_cloudsearch.types.index_field_type
    import capo_cloudsearch.types.int_array_options
    import capo_cloudsearch.types.int_options
    import capo_cloudsearch.types.lat_lon_options
    import capo_cloudsearch.types.literal_array_options
    import capo_cloudsearch.types.literal_options
    import capo_cloudsearch.types.text_array_options
    import capo_cloudsearch.types.text_options


class IndexField(TypedDict, closed=True):
    index_field_name: "capo_cloudsearch.types.dynamic_field_name.DynamicFieldName"
    """<p>A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field's name defines a pattern that begins or ends with a wildcard. Any document fields that don't map to a regular index field but do match a dynamic field's pattern are configured with the dynamic field's indexing options. </p> <p>Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported. </p> <p>The name <code>score</code> is reserved and cannot be used as a field name. To reference a document's ID, you can use the name <code>_id</code>. </p>"""
    index_field_type: "capo_cloudsearch.types.index_field_type.IndexFieldType"
    int_options: NotRequired["capo_cloudsearch.types.int_options.IntOptions"]
    double_options: NotRequired["capo_cloudsearch.types.double_options.DoubleOptions"]
    literal_options: NotRequired[
        "capo_cloudsearch.types.literal_options.LiteralOptions"
    ]
    text_options: NotRequired["capo_cloudsearch.types.text_options.TextOptions"]
    date_options: NotRequired["capo_cloudsearch.types.date_options.DateOptions"]
    lat_lon_options: NotRequired["capo_cloudsearch.types.lat_lon_options.LatLonOptions"]
    int_array_options: NotRequired[
        "capo_cloudsearch.types.int_array_options.IntArrayOptions"
    ]
    double_array_options: NotRequired[
        "capo_cloudsearch.types.double_array_options.DoubleArrayOptions"
    ]
    literal_array_options: NotRequired[
        "capo_cloudsearch.types.literal_array_options.LiteralArrayOptions"
    ]
    text_array_options: NotRequired[
        "capo_cloudsearch.types.text_array_options.TextArrayOptions"
    ]
    date_array_options: NotRequired[
        "capo_cloudsearch.types.date_array_options.DateArrayOptions"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IndexField, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}IndexFieldName", str(value["index_field_name"])))
    import capo_cloudsearch.types.index_field_type

    capo_cloudsearch.types.index_field_type.serialize_query(
        value["index_field_type"], pairs, f"{key_prefix}IndexFieldType"
    )
    if "int_options" in value:
        import capo_cloudsearch.types.int_options

        capo_cloudsearch.types.int_options.serialize_query(
            value["int_options"], pairs, f"{key_prefix}IntOptions"
        )
    if "double_options" in value:
        import capo_cloudsearch.types.double_options

        capo_cloudsearch.types.double_options.serialize_query(
            value["double_options"], pairs, f"{key_prefix}DoubleOptions"
        )
    if "literal_options" in value:
        import capo_cloudsearch.types.literal_options

        capo_cloudsearch.types.literal_options.serialize_query(
            value["literal_options"], pairs, f"{key_prefix}LiteralOptions"
        )
    if "text_options" in value:
        import capo_cloudsearch.types.text_options

        capo_cloudsearch.types.text_options.serialize_query(
            value["text_options"], pairs, f"{key_prefix}TextOptions"
        )
    if "date_options" in value:
        import capo_cloudsearch.types.date_options

        capo_cloudsearch.types.date_options.serialize_query(
            value["date_options"], pairs, f"{key_prefix}DateOptions"
        )
    if "lat_lon_options" in value:
        import capo_cloudsearch.types.lat_lon_options

        capo_cloudsearch.types.lat_lon_options.serialize_query(
            value["lat_lon_options"], pairs, f"{key_prefix}LatLonOptions"
        )
    if "int_array_options" in value:
        import capo_cloudsearch.types.int_array_options

        capo_cloudsearch.types.int_array_options.serialize_query(
            value["int_array_options"], pairs, f"{key_prefix}IntArrayOptions"
        )
    if "double_array_options" in value:
        import capo_cloudsearch.types.double_array_options

        capo_cloudsearch.types.double_array_options.serialize_query(
            value["double_array_options"], pairs, f"{key_prefix}DoubleArrayOptions"
        )
    if "literal_array_options" in value:
        import capo_cloudsearch.types.literal_array_options

        capo_cloudsearch.types.literal_array_options.serialize_query(
            value["literal_array_options"], pairs, f"{key_prefix}LiteralArrayOptions"
        )
    if "text_array_options" in value:
        import capo_cloudsearch.types.text_array_options

        capo_cloudsearch.types.text_array_options.serialize_query(
            value["text_array_options"], pairs, f"{key_prefix}TextArrayOptions"
        )
    if "date_array_options" in value:
        import capo_cloudsearch.types.date_array_options

        capo_cloudsearch.types.date_array_options.serialize_query(
            value["date_array_options"], pairs, f"{key_prefix}DateArrayOptions"
        )


def deserialize_query(el: Element) -> IndexField:
    out: IndexField = {}  # type: ignore[typeddict-item]
    child_index_field_name = el.find("IndexFieldName")
    if child_index_field_name is not None:
        out["index_field_name"] = str(child_index_field_name.text or "")
    else:
        out["index_field_name"] = ""
    child_index_field_type = el.find("IndexFieldType")
    if child_index_field_type is not None:
        import capo_cloudsearch.types.index_field_type

        out["index_field_type"] = (
            capo_cloudsearch.types.index_field_type.deserialize_query(
                child_index_field_type
            )
        )
    else:
        import typing

        out["index_field_type"] = typing.cast(
            "capo_cloudsearch.types.index_field_type.IndexFieldType", ""
        )
    child_int_options = el.find("IntOptions")
    if child_int_options is not None:
        import capo_cloudsearch.types.int_options

        out["int_options"] = capo_cloudsearch.types.int_options.deserialize_query(
            child_int_options
        )
    child_double_options = el.find("DoubleOptions")
    if child_double_options is not None:
        import capo_cloudsearch.types.double_options

        out["double_options"] = capo_cloudsearch.types.double_options.deserialize_query(
            child_double_options
        )
    child_literal_options = el.find("LiteralOptions")
    if child_literal_options is not None:
        import capo_cloudsearch.types.literal_options

        out["literal_options"] = (
            capo_cloudsearch.types.literal_options.deserialize_query(
                child_literal_options
            )
        )
    child_text_options = el.find("TextOptions")
    if child_text_options is not None:
        import capo_cloudsearch.types.text_options

        out["text_options"] = capo_cloudsearch.types.text_options.deserialize_query(
            child_text_options
        )
    child_date_options = el.find("DateOptions")
    if child_date_options is not None:
        import capo_cloudsearch.types.date_options

        out["date_options"] = capo_cloudsearch.types.date_options.deserialize_query(
            child_date_options
        )
    child_lat_lon_options = el.find("LatLonOptions")
    if child_lat_lon_options is not None:
        import capo_cloudsearch.types.lat_lon_options

        out["lat_lon_options"] = (
            capo_cloudsearch.types.lat_lon_options.deserialize_query(
                child_lat_lon_options
            )
        )
    child_int_array_options = el.find("IntArrayOptions")
    if child_int_array_options is not None:
        import capo_cloudsearch.types.int_array_options

        out["int_array_options"] = (
            capo_cloudsearch.types.int_array_options.deserialize_query(
                child_int_array_options
            )
        )
    child_double_array_options = el.find("DoubleArrayOptions")
    if child_double_array_options is not None:
        import capo_cloudsearch.types.double_array_options

        out["double_array_options"] = (
            capo_cloudsearch.types.double_array_options.deserialize_query(
                child_double_array_options
            )
        )
    child_literal_array_options = el.find("LiteralArrayOptions")
    if child_literal_array_options is not None:
        import capo_cloudsearch.types.literal_array_options

        out["literal_array_options"] = (
            capo_cloudsearch.types.literal_array_options.deserialize_query(
                child_literal_array_options
            )
        )
    child_text_array_options = el.find("TextArrayOptions")
    if child_text_array_options is not None:
        import capo_cloudsearch.types.text_array_options

        out["text_array_options"] = (
            capo_cloudsearch.types.text_array_options.deserialize_query(
                child_text_array_options
            )
        )
    child_date_array_options = el.find("DateArrayOptions")
    if child_date_array_options is not None:
        import capo_cloudsearch.types.date_array_options

        out["date_array_options"] = (
            capo_cloudsearch.types.date_array_options.deserialize_query(
                child_date_array_options
            )
        )
    return out
