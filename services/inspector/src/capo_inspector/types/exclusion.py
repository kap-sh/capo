"""Generated from Smithy shape ``com.amazonaws.inspector#Exclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.attribute_list
    import capo_inspector.types.scope_list
    import capo_inspector.types.text


class Exclusion(TypedDict, closed=True):
    arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the exclusion.</p>"""
    title: "capo_inspector.types.text.Text"
    """<p>The name of the exclusion.</p>"""
    description: "capo_inspector.types.text.Text"
    """<p>The description of the exclusion.</p>"""
    recommendation: "capo_inspector.types.text.Text"
    """<p>The recommendation for the exclusion.</p>"""
    scopes: "capo_inspector.types.scope_list.ScopeList"
    """<p>The AWS resources for which the exclusion pertains.</p>"""
    attributes: NotRequired["capo_inspector.types.attribute_list.AttributeList"]
    """<p>The system-defined attributes for the exclusion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Exclusion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    out["description"] = value["description"]
    out["recommendation"] = value["recommendation"]
    import capo_inspector.types.scope_list

    out["scopes"] = capo_inspector.types.scope_list.serialize_aws_json_1_1(
        value["scopes"]
    )
    if "attributes" in value:
        import capo_inspector.types.attribute_list

        out["attributes"] = capo_inspector.types.attribute_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Exclusion:
    out: Exclusion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    else:
        out["recommendation"] = ""
    if data.get("scopes") is not None:
        import capo_inspector.types.scope_list

        out["scopes"] = capo_inspector.types.scope_list.deserialize_aws_json_1_1(
            data["scopes"]
        )
    else:
        out["scopes"] = []
    if data.get("attributes") is not None:
        import capo_inspector.types.attribute_list

        out["attributes"] = (
            capo_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    return out
