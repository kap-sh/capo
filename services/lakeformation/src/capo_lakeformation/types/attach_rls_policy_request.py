"""Generated from Smithy shape ``com.amazonaws.lakeformation#AttachRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.resource


class AttachRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the row-level security policy to attach.</p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The resource to which the row-level security policy is attached.</p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal to which the row-level security policy applies.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    """<p>A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.</p>"""
    set_default: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether this policy becomes the default row-level security policy for the resource. The default policy applies to all principals by default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachRLSPolicyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_lakeformation.types.resource

    out["Resource"] = capo_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "set_default" in value:
        out["SetDefault"] = value["set_default"]
    return out


def deserialize_json(data: dict) -> AttachRLSPolicyRequest:
    out: AttachRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AttachRLSPolicyRequest.name required")
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("AttachRLSPolicyRequest.resource required")
    if data.get("Principal") is not None:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if data.get("Condition") is not None:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if data.get("SetDefault") is not None:
        out["set_default"] = data["SetDefault"]
    return out
