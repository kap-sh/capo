"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.application_name
    import capo_appintegrations.types.application_namespace
    import capo_appintegrations.types.application_type
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.boolean
    import capo_appintegrations.types.region_name
    import capo_appintegrations.types.timestamp
    import capo_appintegrations.types.uuid


class ApplicationSummary(TypedDict, closed=True):
    arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Application.</p>"""
    id: NotRequired["capo_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier for the Application.</p>"""
    name: NotRequired["capo_appintegrations.types.application_name.ApplicationName"]
    """<p>The name of the application.</p>"""
    namespace: NotRequired[
        "capo_appintegrations.types.application_namespace.ApplicationNamespace"
    ]
    """<p>The namespace of the application.</p>"""
    created_time: NotRequired["capo_appintegrations.types.timestamp.Timestamp"]
    """<p>The time when the application was created.</p>"""
    last_modified_time: NotRequired["capo_appintegrations.types.timestamp.Timestamp"]
    """<p>The time when the application was last modified.</p>"""
    last_modified_region: NotRequired[
        "capo_appintegrations.types.region_name.RegionName"
    ]
    """<p>The Amazon Web Services Region where the application was last modified.</p>"""
    is_service: "capo_appintegrations.types.boolean.Boolean"
    """<p>Indicates whether the application is a service.</p>"""
    application_type: NotRequired[
        "capo_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "created_time" in value:
        import capo_appintegrations.types.timestamp

        out["CreatedTime"] = capo_appintegrations.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_appintegrations.types.timestamp

        out["LastModifiedTime"] = capo_appintegrations.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    out["IsService"] = value.get("is_service", False)
    if "application_type" in value:
        import capo_appintegrations.types.application_type

        out["ApplicationType"] = (
            capo_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("CreatedTime") is not None:
        import capo_appintegrations.types.timestamp

        out["created_time"] = capo_appintegrations.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_appintegrations.types.timestamp

        out["last_modified_time"] = (
            capo_appintegrations.types.timestamp.deserialize_json(
                data["LastModifiedTime"]
            )
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("IsService") is not None:
        out["is_service"] = data["IsService"]
    else:
        out["is_service"] = False
    if data.get("ApplicationType") is not None:
        import capo_appintegrations.types.application_type

        out["application_type"] = (
            capo_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    return out
