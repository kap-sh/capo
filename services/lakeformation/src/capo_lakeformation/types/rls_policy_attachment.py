"""Generated from Smithy shape ``com.amazonaws.lakeformation#RLSPolicyAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.resource


class RLSPolicyAttachment(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog that contains the attachment. By default, the account ID.</p>"""
    policy_name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name of the attached row-level security policy.</p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal to which the attached policy applies.</p>"""
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>The resource to which the policy is attached.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    """<p>A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.</p>"""
    default_rls_policy: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether this attachment is the default row-level security policy for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RLSPolicyAttachment) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "default_rls_policy" in value:
        out["DefaultRLSPolicy"] = value["default_rls_policy"]
    return out


def deserialize_json(data: dict) -> RLSPolicyAttachment:
    out: RLSPolicyAttachment = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("Principal") is not None:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if data.get("Condition") is not None:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if data.get("DefaultRLSPolicy") is not None:
        out["default_rls_policy"] = data["DefaultRLSPolicy"]
    return out
