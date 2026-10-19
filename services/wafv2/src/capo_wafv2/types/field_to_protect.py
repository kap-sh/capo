"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToProtect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_protect_keys
    import capo_wafv2.types.field_to_protect_type


class FieldToProtect(TypedDict, closed=True):
    field_type: "capo_wafv2.types.field_to_protect_type.FieldToProtectType"
    """<p>Specifies the web request component type to protect. </p>"""
    field_keys: NotRequired["capo_wafv2.types.field_to_protect_keys.FieldToProtectKeys"]
    """<p>Specifies the keys to protect for the specified field type.</p> <p>Required for <code>SINGLE_HEADER</code>, <code>SINGLE_COOKIE</code>, and <code>SINGLE_QUERY_ARGUMENT</code>: provide a non-empty array naming the specific headers, cookies, or query arguments to protect. There is no option to protect all keys of these field types, so enumerate each key you intend to protect.</p> <p>Must be omitted for <code>QUERY_STRING</code> and <code>BODY</code>: the entire component is protected and these field types take no keys. Supplying <code>FieldKeys</code> for them is rejected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldToProtect) -> dict:
    out: dict = {}
    import capo_wafv2.types.field_to_protect_type

    out["FieldType"] = capo_wafv2.types.field_to_protect_type.serialize_aws_json_1_1(
        value["field_type"]
    )
    if "field_keys" in value:
        import capo_wafv2.types.field_to_protect_keys

        out["FieldKeys"] = (
            capo_wafv2.types.field_to_protect_keys.serialize_aws_json_1_1(
                value["field_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldToProtect:
    out: FieldToProtect = {}  # type: ignore[typeddict-item]
    if data.get("FieldType") is not None:
        import capo_wafv2.types.field_to_protect_type

        out["field_type"] = (
            capo_wafv2.types.field_to_protect_type.deserialize_aws_json_1_1(
                data["FieldType"]
            )
        )
    else:
        import typing

        out["field_type"] = typing.cast(
            "capo_wafv2.types.field_to_protect_type.FieldToProtectType", ""
        )
    if data.get("FieldKeys") is not None:
        import capo_wafv2.types.field_to_protect_keys

        out["field_keys"] = (
            capo_wafv2.types.field_to_protect_keys.deserialize_aws_json_1_1(
                data["FieldKeys"]
            )
        )
    return out
