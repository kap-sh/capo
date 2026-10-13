"""Generated from Smithy shape ``com.amazonaws.gamelift#GetInstanceAccessOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.instance_access


class GetInstanceAccessOutput(TypedDict, closed=True):
    instance_access: NotRequired["capo_gamelift.types.instance_access.InstanceAccess"]
    """<p>The connection information for a fleet instance, including IP address and access credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceAccessOutput) -> dict:
    out: dict = {}
    if "instance_access" in value:
        import capo_gamelift.types.instance_access

        out["InstanceAccess"] = (
            capo_gamelift.types.instance_access.serialize_aws_json_1_1(
                value["instance_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceAccessOutput:
    out: GetInstanceAccessOutput = {}  # type: ignore[typeddict-item]
    if data.get("InstanceAccess") is not None:
        import capo_gamelift.types.instance_access

        out["instance_access"] = (
            capo_gamelift.types.instance_access.deserialize_aws_json_1_1(
                data["InstanceAccess"]
            )
        )
    return out


def redact_sensitive(value: GetInstanceAccessOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_access" in value:
        import capo_gamelift.types.instance_access

        out["instance_access"] = capo_gamelift.types.instance_access.redact_sensitive(
            value["instance_access"]
        )
    return out
