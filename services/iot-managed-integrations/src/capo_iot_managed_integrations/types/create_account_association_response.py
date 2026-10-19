"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateAccountAssociationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_arn
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.association_state
    import capo_iot_managed_integrations.types.o_auth_authorization_url_output


class CreateAccountAssociationResponse(TypedDict, closed=True):
    o_auth_authorization_url: "capo_iot_managed_integrations.types.o_auth_authorization_url_output.OAuthAuthorizationUrlOutput"
    """<p>Third-party IoT platform OAuth authorization server URL backed with all the required parameters to perform end-user authentication. This field will be empty when using General Authorization flows that do not require OAuth.</p>"""
    account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    """<p>The identifier for the account association request.</p>"""
    association_state: (
        "capo_iot_managed_integrations.types.association_state.AssociationState"
    )
    """<p>The current state of the account association request.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.account_association_arn.AccountAssociationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the account association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountAssociationResponse) -> dict:
    out: dict = {}
    out["OAuthAuthorizationUrl"] = value.get("o_auth_authorization_url", "")
    out["AccountAssociationId"] = value["account_association_id"]
    import capo_iot_managed_integrations.types.association_state

    out["AssociationState"] = (
        capo_iot_managed_integrations.types.association_state.serialize_json(
            value["association_state"]
        )
    )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateAccountAssociationResponse:
    out: CreateAccountAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("OAuthAuthorizationUrl") is not None:
        out["o_auth_authorization_url"] = data["OAuthAuthorizationUrl"]
    else:
        out["o_auth_authorization_url"] = ""
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    else:
        out["account_association_id"] = ""
    if data.get("AssociationState") is not None:
        import capo_iot_managed_integrations.types.association_state

        out["association_state"] = (
            capo_iot_managed_integrations.types.association_state.deserialize_json(
                data["AssociationState"]
            )
        )
    else:
        import typing

        out["association_state"] = typing.cast(
            "capo_iot_managed_integrations.types.association_state.AssociationState", ""
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out


def redact_sensitive(value: CreateAccountAssociationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth_authorization_url" in value:
        out["o_auth_authorization_url"] = "*** Sensitive Data Redacted ***"
    return out
