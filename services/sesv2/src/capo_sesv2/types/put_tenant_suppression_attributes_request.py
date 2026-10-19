"""Generated from Smithy shape ``com.amazonaws.sesv2#PutTenantSuppressionAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.suppression_list_reasons
    import capo_sesv2.types.suppression_list_scope
    import capo_sesv2.types.tenant_name


class PutTenantSuppressionAttributesRequest(TypedDict, closed=True):
    tenant_name: "capo_sesv2.types.tenant_name.TenantName"
    """<p>The name of the tenant to configure suppression list preferences for.</p>"""
    suppressed_reasons: NotRequired[
        "capo_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses are automatically added to the suppression list for the tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    suppression_scope: NotRequired[
        "capo_sesv2.types.suppression_list_scope.SuppressionListScope"
    ]
    """<p>The suppression scope for the tenant. Specify <code>TENANT</code> to use the tenant's own suppression list, or <code>ACCOUNT</code> to use the account-level suppression list.</p> <note> <p>If you don't specify a suppression scope, the tenant defaults to <code>ACCOUNT</code> scope and uses the account-level suppression list.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTenantSuppressionAttributesRequest) -> dict:
    out: dict = {}
    out["TenantName"] = value["tenant_name"]
    if "suppressed_reasons" in value:
        import capo_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            capo_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "suppression_scope" in value:
        import capo_sesv2.types.suppression_list_scope

        out["SuppressionScope"] = (
            capo_sesv2.types.suppression_list_scope.serialize_json(
                value["suppression_scope"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutTenantSuppressionAttributesRequest:
    out: PutTenantSuppressionAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TenantName") is not None:
        out["tenant_name"] = data["TenantName"]
    else:
        out["tenant_name"] = ""
    if data.get("SuppressedReasons") is not None:
        import capo_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            capo_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if data.get("SuppressionScope") is not None:
        import capo_sesv2.types.suppression_list_scope

        out["suppression_scope"] = (
            capo_sesv2.types.suppression_list_scope.deserialize_json(
                data["SuppressionScope"]
            )
        )
    return out
