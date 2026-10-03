"""Generated from Smithy shape ``com.amazonaws.connect#CreateUseCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.integration_association_id
    import capo_connect.types.tag_map
    import capo_connect.types.use_case_type


class CreateUseCaseRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    integration_association_id: (
        "capo_connect.types.integration_association_id.IntegrationAssociationId"
    )
    """<p>The identifier for the integration association.</p>"""
    use_case_type: "capo_connect.types.use_case_type.UseCaseType"
    """<p>The type of use case to associate to the integration association. Each integration association can have only one of each use case type.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUseCaseRequest) -> dict:
    out: dict = {}
    import capo_connect.types.use_case_type

    out["UseCaseType"] = capo_connect.types.use_case_type.serialize_json(
        value["use_case_type"]
    )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateUseCaseRequest:
    out: CreateUseCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("UseCaseType") is not None:
        import capo_connect.types.use_case_type

        out["use_case_type"] = capo_connect.types.use_case_type.deserialize_json(
            data["UseCaseType"]
        )
    else:
        raise DeserializationError("CreateUseCaseRequest.use_case_type required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
