"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.resource_detail_arn
    import capo_service_catalog.types.resource_detail_created_time
    import capo_service_catalog.types.resource_detail_description
    import capo_service_catalog.types.resource_detail_id
    import capo_service_catalog.types.resource_detail_name


class ResourceDetail(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.resource_detail_id.ResourceDetailId"]
    """<p>The identifier of the resource.</p>"""
    arn: NotRequired["capo_service_catalog.types.resource_detail_arn.ResourceDetailARN"]
    """<p>The ARN of the resource.</p>"""
    name: NotRequired[
        "capo_service_catalog.types.resource_detail_name.ResourceDetailName"
    ]
    """<p>The name of the resource.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.resource_detail_description.ResourceDetailDescription"
    ]
    """<p>The description of the resource.</p>"""
    created_time: NotRequired[
        "capo_service_catalog.types.resource_detail_created_time.ResourceDetailCreatedTime"
    ]
    """<p>The creation time of the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.resource_detail_created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.resource_detail_created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDetail:
    out: ResourceDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.resource_detail_created_time

        out["created_time"] = (
            capo_service_catalog.types.resource_detail_created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.resource_detail_created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.resource_detail_created_time.serialize_cbor(
                value["created_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResourceDetail:
    out: ResourceDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.resource_detail_created_time

        out["created_time"] = (
            capo_service_catalog.types.resource_detail_created_time.deserialize_cbor(
                data["CreatedTime"]
            )
        )
    return out
