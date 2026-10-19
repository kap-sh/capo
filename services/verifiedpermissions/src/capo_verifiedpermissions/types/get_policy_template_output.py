"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_statement
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_template_description
    import capo_verifiedpermissions.types.policy_template_id
    import capo_verifiedpermissions.types.policy_template_name
    import capo_verifiedpermissions.types.timestamp_format


class GetPolicyTemplateOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the policy template.</p>"""
    policy_template_id: (
        "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>The ID of the policy template.</p>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
    ]
    """<p>The description of the policy template.</p>"""
    statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>The content of the body of the policy template written in the Cedar policy language.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy template was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy template was most recently updated.</p>"""
    name: NotRequired[
        "capo_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
    ]
    """<p>The name of the policy template, if one was assigned when the policy template was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyTemplateOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyTemplateOutput:
    out: GetPolicyTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("policyTemplateId") is not None:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        out["policy_template_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        out["statement"] = ""
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        import datetime

        out["created_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        import datetime

        out["last_updated_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: GetPolicyTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "statement" in value:
        out["statement"] = "*** Sensitive Data Redacted ***"
    return out
