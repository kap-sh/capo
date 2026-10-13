"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePropertiesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_properties
    import capo_ssm.types.next_token


class DescribeInstancePropertiesResult(TypedDict, closed=True):
    instance_properties: NotRequired[
        "capo_ssm.types.instance_properties.InstanceProperties"
    ]
    """<p>Properties for the managed instances.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of properties to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePropertiesResult) -> dict:
    out: dict = {}
    if "instance_properties" in value:
        import capo_ssm.types.instance_properties

        out["InstanceProperties"] = (
            capo_ssm.types.instance_properties.serialize_aws_json_1_1(
                value["instance_properties"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePropertiesResult:
    out: DescribeInstancePropertiesResult = {}  # type: ignore[typeddict-item]
    if data.get("InstanceProperties") is not None:
        import capo_ssm.types.instance_properties

        out["instance_properties"] = (
            capo_ssm.types.instance_properties.deserialize_aws_json_1_1(
                data["InstanceProperties"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeInstancePropertiesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_properties" in value:
        import capo_ssm.types.instance_properties

        out["instance_properties"] = (
            capo_ssm.types.instance_properties.redact_sensitive(
                value["instance_properties"]
            )
        )
    return out
