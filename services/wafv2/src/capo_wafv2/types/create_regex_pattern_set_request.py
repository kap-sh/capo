"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateRegexPatternSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.regular_expression_list
    import capo_wafv2.types.scope
    import capo_wafv2.types.tag_list


class CreateRegexPatternSetRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the set. You cannot change the name after you create the set.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the set that helps with identification. </p>"""
    regular_expression_list: (
        "capo_wafv2.types.regular_expression_list.RegularExpressionList"
    )
    """<p>Array of regular expression strings. </p>"""
    tags: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>An array of key:value pairs to associate with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "description" in value:
        out["Description"] = value["description"]
    import capo_wafv2.types.regular_expression_list

    out["RegularExpressionList"] = (
        capo_wafv2.types.regular_expression_list.serialize_aws_json_1_1(
            value["regular_expression_list"]
        )
    )
    if "tags" in value:
        import capo_wafv2.types.tag_list

        out["Tags"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegexPatternSetRequest:
    out: CreateRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RegularExpressionList") is not None:
        import capo_wafv2.types.regular_expression_list

        out["regular_expression_list"] = (
            capo_wafv2.types.regular_expression_list.deserialize_aws_json_1_1(
                data["RegularExpressionList"]
            )
        )
    else:
        out["regular_expression_list"] = []
    if data.get("Tags") is not None:
        import capo_wafv2.types.tag_list

        out["tags"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
