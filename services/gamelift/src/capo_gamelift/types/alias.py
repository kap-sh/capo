"""Generated from Smithy shape ``com.amazonaws.gamelift#Alias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias_arn
    import capo_gamelift.types.alias_id
    import capo_gamelift.types.free_text
    import capo_gamelift.types.non_blank_and_length_constraint_string
    import capo_gamelift.types.routing_strategy
    import capo_gamelift.types.timestamp


class Alias(TypedDict, closed=True):
    alias_id: NotRequired["capo_gamelift.types.alias_id.AliasId"]
    """<p>A unique identifier for the alias. Alias IDs are unique within a Region.</p>"""
    name: NotRequired[
        "capo_gamelift.types.non_blank_and_length_constraint_string.NonBlankAndLengthConstraintString"
    ]
    """<p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>"""
    alias_arn: NotRequired["capo_gamelift.types.alias_arn.AliasArn"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers alias resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. In a GameLift alias ARN, the resource ID matches the alias ID value.</p>"""
    description: NotRequired["capo_gamelift.types.free_text.FreeText"]
    """<p>A human-readable description of an alias.</p>"""
    routing_strategy: NotRequired[
        "capo_gamelift.types.routing_strategy.RoutingStrategy"
    ]
    """<p>The routing configuration, including routing type and fleet target, for the alias. </p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    last_updated_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alias) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "alias_arn" in value:
        out["AliasArn"] = value["alias_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_strategy" in value:
        import capo_gamelift.types.routing_strategy

        out["RoutingStrategy"] = (
            capo_gamelift.types.routing_strategy.serialize_aws_json_1_1(
                value["routing_strategy"]
            )
        )
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_gamelift.types.timestamp

        out["LastUpdatedTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Alias:
    out: Alias = {}  # type: ignore[typeddict-item]
    if data.get("AliasId") is not None:
        out["alias_id"] = data["AliasId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AliasArn") is not None:
        out["alias_arn"] = data["AliasArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoutingStrategy") is not None:
        import capo_gamelift.types.routing_strategy

        out["routing_strategy"] = (
            capo_gamelift.types.routing_strategy.deserialize_aws_json_1_1(
                data["RoutingStrategy"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_gamelift.types.timestamp

        out["last_updated_time"] = (
            capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
