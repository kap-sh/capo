"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ListResourcesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.handler_next_token
    import capo_cloudcontrol.types.resource_descriptions
    import capo_cloudcontrol.types.type_name


class ListResourcesOutput(TypedDict, closed=True):
    type_name: NotRequired["capo_cloudcontrol.types.type_name.TypeName"]
    """<p>The name of the resource type.</p>"""
    resource_descriptions: NotRequired[
        "capo_cloudcontrol.types.resource_descriptions.ResourceDescriptions"
    ]
    """<p>Information about the specified resources, including primary identifier and resource model.</p>"""
    next_token: NotRequired[
        "capo_cloudcontrol.types.handler_next_token.HandlerNextToken"
    ]
    """<p>If the request doesn't return all of the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>ListResources</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourcesOutput) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "resource_descriptions" in value:
        import capo_cloudcontrol.types.resource_descriptions

        out["ResourceDescriptions"] = (
            capo_cloudcontrol.types.resource_descriptions.serialize_aws_json_1_0(
                value["resource_descriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourcesOutput:
    out: ListResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("ResourceDescriptions") is not None:
        import capo_cloudcontrol.types.resource_descriptions

        out["resource_descriptions"] = (
            capo_cloudcontrol.types.resource_descriptions.deserialize_aws_json_1_0(
                data["ResourceDescriptions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListResourcesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_descriptions" in value:
        import capo_cloudcontrol.types.resource_descriptions

        out["resource_descriptions"] = (
            capo_cloudcontrol.types.resource_descriptions.redact_sensitive(
                value["resource_descriptions"]
            )
        )
    return out
