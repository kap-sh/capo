"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateVersionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_proton.types.description
    import capo_proton.types.environment_template_version_arn
    import capo_proton.types.resource_name
    import capo_proton.types.status_message
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_status


class EnvironmentTemplateVersionSummary(TypedDict, closed=True):
    template_name: "capo_proton.types.resource_name.ResourceName"
    """<p>The name of the environment template.</p>"""
    major_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The latest major version that's associated with the version of an environment template.</p>"""
    minor_version: "capo_proton.types.template_version_part.TemplateVersionPart"
    """<p>The version of an environment template.</p>"""
    recommended_minor_version: NotRequired[
        "capo_proton.types.template_version_part.TemplateVersionPart"
    ]
    """<p>The recommended minor version of the environment template.</p>"""
    status: "capo_proton.types.template_version_status.TemplateVersionStatus"
    """<p>The status of the version of an environment template.</p>"""
    status_message: NotRequired["capo_proton.types.status_message.StatusMessage"]
    """<p>The status message of the version of an environment template.</p>"""
    description: NotRequired["capo_proton.types.description.Description"]
    """<p>A description of the version of an environment template.</p>"""
    arn: "capo_proton.types.environment_template_version_arn.EnvironmentTemplateVersionArn"
    """<p>The Amazon Resource Name (ARN) of the version of an environment template.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the version of an environment template was created.</p>"""
    last_modified_at: "datetime.datetime"
    """<p>The time when the version of an environment template was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateVersionSummary) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    out["majorVersion"] = value["major_version"]
    out["minorVersion"] = value["minor_version"]
    if "recommended_minor_version" in value:
        out["recommendedMinorVersion"] = value["recommended_minor_version"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "description" in value:
        out["description"] = value["description"]
    out["arn"] = value["arn"]
    import capo_proton.types._prelude.timestamp

    out["createdAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import capo_proton.types._prelude.timestamp

    out["lastModifiedAt"] = capo_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["last_modified_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnvironmentTemplateVersionSummary:
    out: EnvironmentTemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError(
            "EnvironmentTemplateVersionSummary.template_name required"
        )
    if data.get("majorVersion") is not None:
        out["major_version"] = data["majorVersion"]
    else:
        raise DeserializationError(
            "EnvironmentTemplateVersionSummary.major_version required"
        )
    if data.get("minorVersion") is not None:
        out["minor_version"] = data["minorVersion"]
    else:
        raise DeserializationError(
            "EnvironmentTemplateVersionSummary.minor_version required"
        )
    if data.get("recommendedMinorVersion") is not None:
        out["recommended_minor_version"] = data["recommendedMinorVersion"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EnvironmentTemplateVersionSummary.status required")
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EnvironmentTemplateVersionSummary.arn required")
    if data.get("createdAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["created_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentTemplateVersionSummary.created_at required"
        )
    if data.get("lastModifiedAt") is not None:
        import capo_proton.types._prelude.timestamp

        out["last_modified_at"] = (
            capo_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedAt"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentTemplateVersionSummary.last_modified_at required"
        )
    return out


def redact_sensitive(value: EnvironmentTemplateVersionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "status_message" in value:
        out["status_message"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
