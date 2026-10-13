"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.resource_description
    import capo_cloudcontrol.types.type_name


class GetResourceOutput(TypedDict, closed=True):
    type_name: NotRequired["capo_cloudcontrol.types.type_name.TypeName"]
    """<p>The name of the resource type.</p>"""
    resource_description: NotRequired[
        "capo_cloudcontrol.types.resource_description.ResourceDescription"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceOutput) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "resource_description" in value:
        import capo_cloudcontrol.types.resource_description

        out["ResourceDescription"] = (
            capo_cloudcontrol.types.resource_description.serialize_aws_json_1_0(
                value["resource_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceOutput:
    out: GetResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("ResourceDescription") is not None:
        import capo_cloudcontrol.types.resource_description

        out["resource_description"] = (
            capo_cloudcontrol.types.resource_description.deserialize_aws_json_1_0(
                data["ResourceDescription"]
            )
        )
    return out


def redact_sensitive(value: GetResourceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_description" in value:
        import capo_cloudcontrol.types.resource_description

        out["resource_description"] = (
            capo_cloudcontrol.types.resource_description.redact_sensitive(
                value["resource_description"]
            )
        )
    return out
