"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.description
    import capo_proton.types.display_name
    import capo_proton.types.environment_template_arn
    import capo_proton.types.full_template_version_number
    import capo_proton.types.provisioning
    import capo_proton.types.resource_name


class EnvironmentTemplateSummary(TypedDict, closed=True):
    name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    arn: "capo_proton.types.environment_template_arn.EnvironmentTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the environment template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the environment template was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the environment template was last modified.</p>"""
    display_name: NotRequired["capo_proton.types.display_name.DisplayName"]
    """<p>The name of the environment template as displayed in the developer interface.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the environment template.</p>"""
    recommended_version: NotRequired[
        "capo_proton.types.full_template_version_number.FullTemplateVersionNumber"
    ]
    """<p>The recommended version of the environment template.</p>"""
    provisioning: NotRequired["capo_proton.types.provisioning.Provisioning"]
    """<p>When included, indicates that the environment template is for customer provisioned and managed infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "recommended_version" in value:
        out["recommendedVersion"] = value["recommended_version"]
    if "provisioning" in value:
        out["provisioning"] = value["provisioning"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentTemplateSummary:
    out: EnvironmentTemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentTemplateSummary.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnvironmentTemplateSummary.arn required")
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("EnvironmentTemplateSummary.created_at required")
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentTemplateSummary.last_modified_at required"
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("recommendedVersion") is not None:
        out["recommended_version"] = data["recommendedVersion"]
    if data.get("provisioning") is not None:
        out["provisioning"] = data["provisioning"]
    return out


def redact_sensitive(value: EnvironmentTemplateSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
