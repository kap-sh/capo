"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PutSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.schema_definition


class PutSchemaInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store in which to place the schema.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    definition: "capo_verifiedpermissions.types.schema_definition.SchemaDefinition"
    """<p>Specifies the definition of the schema to be stored. The schema definition must be written in Cedar schema JSON.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutSchemaInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    import capo_verifiedpermissions.types.schema_definition

    out["definition"] = (
        capo_verifiedpermissions.types.schema_definition.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutSchemaInput:
    out: PutSchemaInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PutSchemaInput.policy_store_id required")
    if data.get("definition") is not None:
        import capo_verifiedpermissions.types.schema_definition

        out["definition"] = (
            capo_verifiedpermissions.types.schema_definition.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("PutSchemaInput.definition required")
    return out
