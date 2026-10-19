"""Generated from Smithy shape ``com.amazonaws.wafv2#LabelMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.label_match_key
    import capo_wafv2.types.label_match_scope


class LabelMatchStatement(TypedDict, closed=True):
    scope: "capo_wafv2.types.label_match_scope.LabelMatchScope"
    """<p>Specify whether you want to match using the label name or just the namespace. </p>"""
    key: "capo_wafv2.types.label_match_key.LabelMatchKey"
    """<p>The string to match against. The setting you provide for this depends on the match statement's <code>Scope</code> setting: </p> <ul> <li> <p>If the <code>Scope</code> indicates <code>LABEL</code>, then this specification must include the name and can include any number of preceding namespace specifications and prefix up to providing the fully qualified label name. </p> </li> <li> <p>If the <code>Scope</code> indicates <code>NAMESPACE</code>, then this specification can include any number of contiguous namespace strings, and can include the entire label namespace prefix from the rule group or web ACL where the label originates.</p> </li> </ul> <p>Labels are case sensitive and components of a label must be separated by colon, for example <code>NS1:NS2:name</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelMatchStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.label_match_scope

    out["Scope"] = capo_wafv2.types.label_match_scope.serialize_aws_json_1_1(
        value["scope"]
    )
    out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelMatchStatement:
    out: LabelMatchStatement = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_wafv2.types.label_match_scope

        out["scope"] = capo_wafv2.types.label_match_scope.deserialize_aws_json_1_1(
            data["Scope"]
        )
    else:
        import typing

        out["scope"] = typing.cast(
            "capo_wafv2.types.label_match_scope.LabelMatchScope", ""
        )
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    return out
