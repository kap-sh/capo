"""Generated from Smithy shape ``com.amazonaws.lambda#AliasConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.alias
    import capo_lambda.types.alias_routing_configuration
    import capo_lambda.types.description
    import capo_lambda.types.function_arn
    import capo_lambda.types.string
    import capo_lambda.types.version


class AliasConfiguration(TypedDict, closed=True):
    alias_arn: NotRequired["capo_lambda.types.function_arn.FunctionArn"]
    """<p>The Amazon Resource Name (ARN) of the alias.</p>"""
    name: NotRequired["capo_lambda.types.alias.Alias"]
    """<p>The name of the alias.</p>"""
    function_version: NotRequired["capo_lambda.types.version.Version"]
    """<p>The function version that the alias invokes.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_config: NotRequired[
        "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html">routing configuration</a> of the alias.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>A unique identifier that changes when you update the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfiguration) -> dict:
    out: dict = {}
    if "alias_arn" in value:
        out["AliasArn"] = value["alias_arn"]
    if "name" in value:
        out["Name"] = value["name"]
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


def deserialize_json(data: dict) -> AliasConfiguration:
    out: AliasConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AliasArn") is not None:
        out["alias_arn"] = data["AliasArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
