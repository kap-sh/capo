"""Generated from Smithy shape ``com.amazonaws.lakeformation#DetachRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.resource


class DetachRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the row-level security policy to detach.</p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The resource from which the row-level security policy is detached.</p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal for which the row-level security policy is detached.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    """<p>A Lake Formation condition, which applies to the row-level security policy attachment and contains an expression.</p>"""
    remove_default: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether to remove this policy as the default row-level security policy for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachRLSPolicyRequest) -> dict:
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
    if "remove_default" in value:
        out["RemoveDefault"] = value["remove_default"]
    return out


def deserialize_json(data: dict) -> DetachRLSPolicyRequest:
    out: DetachRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DetachRLSPolicyRequest.name required")
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("DetachRLSPolicyRequest.resource required")
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
    if data.get("RemoveDefault") is not None:
        out["remove_default"] = data["RemoveDefault"]
    return out
