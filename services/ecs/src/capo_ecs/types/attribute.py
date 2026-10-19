"""Generated from Smithy shape ``com.amazonaws.ecs#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.target_type


class Attribute(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    r"""<p>The name of the attribute. The <code>name</code> must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), forward slashes (/), back slashes (\), or periods (.).</p>"""
    value: NotRequired["capo_ecs.types.string.String"]
    r"""<p>The value of the attribute. The <code>value</code> must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), periods (.), at signs (@), forward slashes (/), back slashes (\), colons (:), or spaces. The value can't start or end with a space.</p>"""
    target_type: NotRequired["capo_ecs.types.target_type.TargetType"]
    """<p>The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.</p>"""
    target_id: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    if "target_type" in value:
        import capo_ecs.types.target_type

        out["targetType"] = capo_ecs.types.target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("targetType") is not None:
        import capo_ecs.types.target_type

        out["target_type"] = capo_ecs.types.target_type.deserialize_aws_json_1_1(
            data["targetType"]
        )
    if data.get("targetId") is not None:
        out["target_id"] = data["targetId"]
    return out
