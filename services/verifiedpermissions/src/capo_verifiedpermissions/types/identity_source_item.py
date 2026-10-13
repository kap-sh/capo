"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.configuration_item
    import capo_verifiedpermissions.types.identity_source_id
    import capo_verifiedpermissions.types.identity_source_item_details
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.principal_entity_type
    import capo_verifiedpermissions.types.timestamp_format


class IdentitySourceItem(TypedDict, closed=True):
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the identity source was originally created.</p>"""
    details: NotRequired[
        "capo_verifiedpermissions.types.identity_source_item_details.IdentitySourceItemDetails"
    ]
    """<p>A structure that contains the details of the associated identity provider (IdP).</p>"""
    identity_source_id: (
        "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>The unique identifier of the identity source.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the identity source was most recently updated.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store that contains the identity source.</p>"""
    principal_entity_type: (
        "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    )
    """<p>The Cedar entity type of the principals returned from the IdP associated with this identity source.</p>"""
    configuration: NotRequired[
        "capo_verifiedpermissions.types.configuration_item.ConfigurationItem"
    ]
    """<p>Contains configuration information about an identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceItem) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "details" in value:
        import capo_verifiedpermissions.types.identity_source_item_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_item_details.serialize_aws_json_1_0(
                value["details"]
            )
        )
    out["identitySourceId"] = value["identity_source_id"]
    import capo_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    out["policyStoreId"] = value["policy_store_id"]
    out["principalEntityType"] = value["principal_entity_type"]
    if "configuration" in value:
        import capo_verifiedpermissions.types.configuration_item

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_item.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentitySourceItem:
    out: IdentitySourceItem = {}  # type: ignore[typeddict-item]
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("IdentitySourceItem.created_date required")
    if data.get("details") is not None:
        import capo_verifiedpermissions.types.identity_source_item_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_item_details.deserialize_aws_json_1_0(
                data["details"]
            )
        )
    if data.get("identitySourceId") is not None:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        raise DeserializationError("IdentitySourceItem.identity_source_id required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("IdentitySourceItem.last_updated_date required")
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("IdentitySourceItem.policy_store_id required")
    if data.get("principalEntityType") is not None:
        out["principal_entity_type"] = data["principalEntityType"]
    else:
        raise DeserializationError("IdentitySourceItem.principal_entity_type required")
    if data.get("configuration") is not None:
        import capo_verifiedpermissions.types.configuration_item

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_item.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out


def redact_sensitive(value: IdentitySourceItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_verifiedpermissions.types.identity_source_item_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_item_details.redact_sensitive(
                value["details"]
            )
        )
    if "principal_entity_type" in value:
        out["principal_entity_type"] = "*** Sensitive Data Redacted ***"
    if "configuration" in value:
        import capo_verifiedpermissions.types.configuration_item

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_item.redact_sensitive(
                value["configuration"]
            )
        )
    return out
