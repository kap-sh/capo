"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.search_field_key
    import capo_chime_sdk_messaging.types.search_field_operator
    import capo_chime_sdk_messaging.types.search_field_values


class SearchField(TypedDict, closed=True):
    key: "capo_chime_sdk_messaging.types.search_field_key.SearchFieldKey"
    """<p>An <code>enum</code> value that indicates the key to search the channel on. <code>MEMBERS</code> allows you to search channels based on memberships. You can use it with the <code>EQUALS</code> operator to get channels whose memberships are equal to the specified values, and with the <code>INCLUDES</code> operator to get channels whose memberships include the specified values.</p>"""
    values: "capo_chime_sdk_messaging.types.search_field_values.SearchFieldValues"
    """<p>The values that you want to search for, a list of strings. The values must be <code>AppInstanceUserArns</code> specified as a list of strings.</p> <note> <p>This operation isn't supported for <code>AppInstanceUsers</code> with a large number of memberships.</p> </note>"""
    operator: "capo_chime_sdk_messaging.types.search_field_operator.SearchFieldOperator"
    """<p>The operator used to compare field values, currently <code>EQUALS</code> or <code>INCLUDES</code>. Use the <code>EQUALS</code> operator to find channels whose memberships equal the specified values. Use the <code>INCLUDES</code> operator to find channels whose memberships include the specified values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchField) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.search_field_key

    out["Key"] = capo_chime_sdk_messaging.types.search_field_key.serialize_json(
        value["key"]
    )
    import capo_chime_sdk_messaging.types.search_field_values

    out["Values"] = capo_chime_sdk_messaging.types.search_field_values.serialize_json(
        value["values"]
    )
    import capo_chime_sdk_messaging.types.search_field_operator

    out["Operator"] = (
        capo_chime_sdk_messaging.types.search_field_operator.serialize_json(
            value["operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchField:
    out: SearchField = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_chime_sdk_messaging.types.search_field_key

        out["key"] = capo_chime_sdk_messaging.types.search_field_key.deserialize_json(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_chime_sdk_messaging.types.search_field_key.SearchFieldKey", ""
        )
    if data.get("Values") is not None:
        import capo_chime_sdk_messaging.types.search_field_values

        out["values"] = (
            capo_chime_sdk_messaging.types.search_field_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_chime_sdk_messaging.types.search_field_operator

        out["operator"] = (
            capo_chime_sdk_messaging.types.search_field_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_chime_sdk_messaging.types.search_field_operator.SearchFieldOperator",
            "",
        )
    return out
