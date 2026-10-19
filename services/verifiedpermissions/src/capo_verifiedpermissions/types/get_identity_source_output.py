"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetIdentitySourceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.configuration_detail
    import capo_verifiedpermissions.types.identity_source_details
    import capo_verifiedpermissions.types.identity_source_id
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.principal_entity_type
    import capo_verifiedpermissions.types.timestamp_format


class GetIdentitySourceOutput(TypedDict, closed=True):
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the identity source was originally created.</p>"""
    details: NotRequired[
        "capo_verifiedpermissions.types.identity_source_details.IdentitySourceDetails"
    ]
    """<p>A structure that describes the configuration of the identity source.</p>"""
    identity_source_id: (
        "capo_verifiedpermissions.types.identity_source_id.IdentitySourceId"
    )
    """<p>The ID of the identity source.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the identity source was most recently updated.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the identity source.</p>"""
    principal_entity_type: (
        "capo_verifiedpermissions.types.principal_entity_type.PrincipalEntityType"
    )
    """<p>The data type of principals generated for identities authenticated by this identity source.</p>"""
    configuration: NotRequired[
        "capo_verifiedpermissions.types.configuration_detail.ConfigurationDetail"
    ]
    """<p>Contains configuration information about an identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdentitySourceOutput) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "details" in value:
        import capo_verifiedpermissions.types.identity_source_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_details.serialize_aws_json_1_0(
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
        import capo_verifiedpermissions.types.configuration_detail

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_detail.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdentitySourceOutput:
    out: GetIdentitySourceOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("details") is not None:
        import capo_verifiedpermissions.types.identity_source_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_details.deserialize_aws_json_1_0(
                data["details"]
            )
        )
    if data.get("identitySourceId") is not None:
        out["identity_source_id"] = data["identitySourceId"]
    else:
        out["identity_source_id"] = ""
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
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("principalEntityType") is not None:
        out["principal_entity_type"] = data["principalEntityType"]
    else:
        out["principal_entity_type"] = ""
    if data.get("configuration") is not None:
        import capo_verifiedpermissions.types.configuration_detail

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_detail.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    return out


def redact_sensitive(value: GetIdentitySourceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_verifiedpermissions.types.identity_source_details

        out["details"] = (
            capo_verifiedpermissions.types.identity_source_details.redact_sensitive(
                value["details"]
            )
        )
    if "principal_entity_type" in value:
        out["principal_entity_type"] = "*** Sensitive Data Redacted ***"
    if "configuration" in value:
        import capo_verifiedpermissions.types.configuration_detail

        out["configuration"] = (
            capo_verifiedpermissions.types.configuration_detail.redact_sensitive(
                value["configuration"]
            )
        )
    return out
