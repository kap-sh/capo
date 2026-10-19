"""Generated from Smithy shape ``com.amazonaws.workmail#PutRetentionPolicyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.folder_configurations
    import capo_workmail.types.organization_id
    import capo_workmail.types.policy_description
    import capo_workmail.types.short_string


class PutRetentionPolicyRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    id: NotRequired["capo_workmail.types.short_string.ShortString"]
    """<p>The retention policy ID.</p>"""
    name: "capo_workmail.types.short_string.ShortString"
    """<p>The retention policy name.</p>"""
    description: NotRequired["capo_workmail.types.policy_description.PolicyDescription"]
    """<p>The retention policy description.</p>"""
    folder_configurations: (
        "capo_workmail.types.folder_configurations.FolderConfigurations"
    )
    """<p>The retention policy folder configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "id" in value:
        out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_workmail.types.folder_configurations

    out["FolderConfigurations"] = (
        capo_workmail.types.folder_configurations.serialize_aws_json_1_1(
            value["folder_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRetentionPolicyRequest:
    out: PutRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FolderConfigurations") is not None:
        import capo_workmail.types.folder_configurations

        out["folder_configurations"] = (
            capo_workmail.types.folder_configurations.deserialize_aws_json_1_1(
                data["FolderConfigurations"]
            )
        )
    else:
        out["folder_configurations"] = []
    return out


def redact_sensitive(value: PutRetentionPolicyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
