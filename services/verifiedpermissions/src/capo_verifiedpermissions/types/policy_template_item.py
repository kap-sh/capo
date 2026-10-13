"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyTemplateItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_template_description
    import capo_verifiedpermissions.types.policy_template_id
    import capo_verifiedpermissions.types.policy_template_name
    import capo_verifiedpermissions.types.timestamp_format


class PolicyTemplateItem(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique identifier of the policy store that contains the template.</p>"""
    policy_template_id: (
        "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>The unique identifier of the policy template.</p>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
    ]
    """<p>The description attached to the policy template.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy template was created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy template was most recently updated.</p>"""
    name: NotRequired[
        "capo_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
    ]
    """<p>The name of the policy template, if one was assigned when the policy template was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyTemplateItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_aws_json_1_0(data: dict) -> PolicyTemplateItem:
    out: PolicyTemplateItem = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PolicyTemplateItem.policy_store_id required")
    if data.get("policyTemplateId") is not None:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        raise DeserializationError("PolicyTemplateItem.policy_template_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PolicyTemplateItem.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("PolicyTemplateItem.last_updated_date required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: PolicyTemplateItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
