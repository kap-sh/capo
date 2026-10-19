"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.component_type_name
    import capo_iottwinmaker.types.description
    import capo_iottwinmaker.types.status
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class ComponentTypeSummary(TypedDict, closed=True):
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The ARN of the component type.</p>"""
    component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The ID of the component type.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was created.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The date and time when the component type was last updated.</p>"""
    description: NotRequired["capo_iottwinmaker.types.description.Description"]
    """<p>The description of the component type.</p>"""
    status: NotRequired["capo_iottwinmaker.types.status.Status"]
    """<p>The current status of the component type.</p>"""
    component_type_name: NotRequired[
        "capo_iottwinmaker.types.component_type_name.ComponentTypeName"
    ]
    """<p>The component type name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentTypeSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["componentTypeId"] = value["component_type_id"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.serialize_json(value["status"])
    if "component_type_name" in value:
        out["componentTypeName"] = value["component_type_name"]
    return out


def deserialize_json(data: dict) -> ComponentTypeSummary:
    out: ComponentTypeSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    else:
        out["component_type_id"] = ""
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_iottwinmaker.types.status

        out["status"] = capo_iottwinmaker.types.status.deserialize_json(data["status"])
    if data.get("componentTypeName") is not None:
        out["component_type_name"] = data["componentTypeName"]
    return out
