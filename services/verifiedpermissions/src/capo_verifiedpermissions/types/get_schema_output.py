"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetSchemaOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.namespace_list
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.schema_json
    import capo_verifiedpermissions.types.timestamp_format


class GetSchemaOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the schema.</p>"""
    schema: "capo_verifiedpermissions.types.schema_json.SchemaJson"
    """<p>The body of the schema, written in Cedar schema JSON.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the schema was most recently updated.</p>"""
    namespaces: NotRequired[
        "capo_verifiedpermissions.types.namespace_list.NamespaceList"
    ]
    """<p>The namespaces of the entities referenced by this schema.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSchemaOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["schema"] = value["schema"]
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
    if "namespaces" in value:
        import capo_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            capo_verifiedpermissions.types.namespace_list.serialize_aws_json_1_0(
                value["namespaces"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSchemaOutput:
    out: GetSchemaOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetSchemaOutput.policy_store_id required")
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("GetSchemaOutput.schema required")
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetSchemaOutput.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("GetSchemaOutput.last_updated_date required")
    if data.get("namespaces") is not None:
        import capo_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            capo_verifiedpermissions.types.namespace_list.deserialize_aws_json_1_0(
                data["namespaces"]
            )
        )
    return out


def redact_sensitive(value: GetSchemaOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schema" in value:
        out["schema"] = "*** Sensitive Data Redacted ***"
    if "namespaces" in value:
        import capo_verifiedpermissions.types.namespace_list

        out["namespaces"] = (
            capo_verifiedpermissions.types.namespace_list.redact_sensitive(
                value["namespaces"]
            )
        )
    return out
