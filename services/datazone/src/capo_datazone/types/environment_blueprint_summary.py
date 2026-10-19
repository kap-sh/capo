"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentBlueprintSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.blueprint_category
    import capo_datazone.types.description
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.provisioning_properties


class EnvironmentBlueprintSummary(TypedDict, closed=True):
    id: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the blueprint.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of the blueprint.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of a blueprint.</p>"""
    provider: "str"
    """<p>The provider of the blueprint.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of the blueprint.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when an environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the blueprint was enabled.</p>"""
    blueprint_category: NotRequired[
        "capo_datazone.types.blueprint_category.BlueprintCategory"
    ]
    """<p>The category of the environment blueprint. The only valid value is <code>TOOLING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentBlueprintSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["provider"] = value["provider"]
    import capo_datazone.types.provisioning_properties

    out["provisioningProperties"] = (
        capo_datazone.types.provisioning_properties.serialize_json(
            value["provisioning_properties"]
        )
    )
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone._protocol.serialize

        out["updatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "blueprint_category" in value:
        import capo_datazone.types.blueprint_category

        out["blueprintCategory"] = (
            capo_datazone.types.blueprint_category.serialize_json(
                value["blueprint_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentBlueprintSummary:
    out: EnvironmentBlueprintSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        import capo_datazone.types._unknown

        out["provisioning_properties"] = (
            capo_datazone.types._unknown.UnknownUnionMember("")
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("blueprintCategory") is not None:
        import capo_datazone.types.blueprint_category

        out["blueprint_category"] = (
            capo_datazone.types.blueprint_category.deserialize_json(
                data["blueprintCategory"]
            )
        )
    return out


def redact_sensitive(value: EnvironmentBlueprintSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
