"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListArtifactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.artifact_category
    import capo_device_farm.types.pagination_token


class ListArtifactsRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The run, job, suite, or test ARN.</p>"""
    type: "capo_device_farm.types.artifact_category.ArtifactCategory"
    """<p>The artifacts' type.</p> <p>Allowed values include:</p> <ul> <li> <p>FILE</p> </li> <li> <p>LOG</p> </li> <li> <p>SCREENSHOT</p> </li> </ul>"""
    next_token: NotRequired["capo_device_farm.types.pagination_token.PaginationToken"]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListArtifactsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_device_farm.types.artifact_category

    out["type"] = capo_device_farm.types.artifact_category.serialize_aws_json_1_1(
        value["type"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListArtifactsRequest:
    out: ListArtifactsRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("type") is not None:
        import capo_device_farm.types.artifact_category

        out["type"] = capo_device_farm.types.artifact_category.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_device_farm.types.artifact_category.ArtifactCategory", ""
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
