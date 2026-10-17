"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.aws_account_id
    import capo_resiliencehubv2.types.aws_region


class Resource(TypedDict, closed=True):
    identifier: "str"
    """<p>The identifier of the resource.</p>"""
    aws_region: NotRequired["capo_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>The AWS Region where the resource is located.</p>"""
    aws_account_id: NotRequired[
        "capo_resiliencehubv2.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID that owns the resource.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("Resource.identifier required")
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    return out
