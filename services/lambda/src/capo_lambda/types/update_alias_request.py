"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.alias
    import capo_lambda.types.alias_routing_configuration
    import capo_lambda.types.description
    import capo_lambda.types.function_name
    import capo_lambda.types.string
    import capo_lambda.types.version_with_latest_published


class UpdateAliasRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    name: "capo_lambda.types.alias.Alias"
    """<p>The name of the alias.</p>"""
    function_version: NotRequired[
        "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>The function version that the alias invokes.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_config: NotRequired[
        "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing">routing configuration</a> of the alias.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAliasRequest) -> dict:
    out: dict = {}
    if "function_version" in value:
        out["FunctionVersion"] = value["function_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_config" in value:
        import capo_lambda.types.alias_routing_configuration

        out["RoutingConfig"] = (
            capo_lambda.types.alias_routing_configuration.serialize_json(
                value["routing_config"]
            )
        )
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> UpdateAliasRequest:
    out: UpdateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("FunctionVersion") is not None:
        out["function_version"] = data["FunctionVersion"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoutingConfig") is not None:
        import capo_lambda.types.alias_routing_configuration

        out["routing_config"] = (
            capo_lambda.types.alias_routing_configuration.deserialize_json(
                data["RoutingConfig"]
            )
        )
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
