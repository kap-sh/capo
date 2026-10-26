"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyOutputItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_definition_detail
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_name
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_type
    import capo_verifiedpermissions.types.timestamp_format


class BatchGetPolicyOutputItem(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store where the policy you want information about is stored.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The identifier of the policy you want information about.</p>"""
    policy_type: "capo_verifiedpermissions.types.policy_type.PolicyType"
    """<p>The type of the policy. This is one of the following values:</p> <ul> <li> <p> <code>STATIC</code> </p> </li> <li> <p> <code>TEMPLATE_LINKED</code> </p> </li> </ul>"""
    definition: (
        "capo_verifiedpermissions.types.policy_definition_detail.PolicyDefinitionDetail"
    )
    """<p>The policy definition of an item in the list of policies returned.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was most recently updated.</p>"""
    name: NotRequired["capo_verifiedpermissions.types.policy_name.PolicyName"]
    """<p>The name of the policy, if one was assigned when the policy was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyOutputItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    import capo_verifiedpermissions.types.policy_type

    out["policyType"] = (
        capo_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
            value["policy_type"]
        )
    )
    import capo_verifiedpermissions.types.policy_definition_detail

    out["definition"] = (
        capo_verifiedpermissions.types.policy_definition_detail.serialize_aws_json_1_0(
            value["definition"]
        )
    )
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


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyOutputItem:
    out: BatchGetPolicyOutputItem = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    if data.get("policyType") is not None:
        import capo_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            capo_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    else:
        import typing

        out["policy_type"] = typing.cast(
            "capo_verifiedpermissions.types.policy_type.PolicyType", ""
        )
    if data.get("definition") is not None:
        import capo_verifiedpermissions.types.policy_definition_detail

        out["definition"] = (
            capo_verifiedpermissions.types.policy_definition_detail.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        out["definition"] = {"$unknown": {"name": ""}}
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


def redact_sensitive(value: BatchGetPolicyOutputItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_verifiedpermissions.types.policy_definition_detail

        out["definition"] = (
            capo_verifiedpermissions.types.policy_definition_detail.redact_sensitive(
                value["definition"]
            )
        )
    return out
