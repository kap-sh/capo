"""Generated from Smithy shape ``com.amazonaws.endusermessaging#JobResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.job_resource_id
    import capo_endusermessaging.types.job_resource_type


class JobResource(TypedDict, closed=True):
    resource_type: "capo_endusermessaging.types.job_resource_type.JobResourceType"
    """<p>The type of the resource that the job created or updated.</p>"""
    resource_id: "capo_endusermessaging.types.job_resource_id.JobResourceId"
    """<p>The identifier of the resource that the job created or updated.</p>"""
    resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobResource) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.job_resource_type

    out["resourceType"] = capo_endusermessaging.types.job_resource_type.serialize_json(
        value["resource_type"]
    )
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> JobResource:
    out: JobResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_endusermessaging.types.job_resource_type

        out["resource_type"] = (
            capo_endusermessaging.types.job_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("JobResource.resource_type required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("JobResource.resource_id required")
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("JobResource.resource_arn required")
    return out
