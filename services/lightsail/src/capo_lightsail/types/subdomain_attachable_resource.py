"""Generated from Smithy shape ``com.amazonaws.lightsail#SubdomainAttachableResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_name


class SubdomainAttachableResource(TypedDict, closed=True):
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the resource.</p>"""
    attached_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the subdomain was associated with the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubdomainAttachableResource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "attached_at" in value:
        import capo_lightsail.types.iso_date

        out["attachedAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["attached_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubdomainAttachableResource:
    out: SubdomainAttachableResource = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("attachedAt") is not None:
        import capo_lightsail.types.iso_date

        out["attached_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["attachedAt"]
        )
    return out
