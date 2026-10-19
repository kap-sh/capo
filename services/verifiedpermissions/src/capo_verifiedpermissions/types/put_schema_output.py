"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PutSchemaOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.namespace_list
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.timestamp_format


class PutSchemaOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique ID of the policy store that contains the schema.</p>"""
    namespaces: "capo_verifiedpermissions.types.namespace_list.NamespaceList"
    """<p>Identifies the namespaces of the entities referenced by this schema.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutSchemaOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    import capo_verifiedpermissions.types.namespace_list

    out["namespaces"] = (
        capo_verifiedpermissions.types.namespace_list.serialize_aws_json_1_0(
            value["namespaces"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> PutSchemaOutput:
    out: PutSchemaOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("namespaces") is not None:
        import capo_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            capo_verifiedpermissions.types.namespace_list.deserialize_aws_json_1_0(
                data["namespaces"]
            )
        )
    else:
        out["namespaces"] = []
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
    return out


def redact_sensitive(value: PutSchemaOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespaces" in value:
        import capo_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            capo_verifiedpermissions.types.namespace_list.redact_sensitive(
                value["namespaces"]
            )
        )
    return out
