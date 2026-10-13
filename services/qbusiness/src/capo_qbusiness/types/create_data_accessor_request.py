"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataAccessorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.action_configuration_list
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.data_accessor_authentication_detail
    import capo_qbusiness.types.data_accessor_name
    import capo_qbusiness.types.principal_role_arn
    import capo_qbusiness.types.tags


class CreateDataAccessorRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    principal: "capo_qbusiness.types.principal_role_arn.PrincipalRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role for the ISV that will be accessing the data.</p>"""
    action_configurations: (
        "capo_qbusiness.types.action_configuration_list.ActionConfigurationList"
    )
    """<p>A list of action configurations specifying the allowed actions and any associated filters.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier you provide to ensure idempotency of the request.</p>"""
    display_name: "capo_qbusiness.types.data_accessor_name.DataAccessorName"
    """<p>A friendly name for the data accessor.</p>"""
    authentication_detail: NotRequired[
        "capo_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>The tags to associate with the data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAccessorRequest) -> dict:
    out: dict = {}
    out["principal"] = value["principal"]
    import capo_qbusiness.types.action_configuration_list

    out["actionConfigurations"] = (
        capo_qbusiness.types.action_configuration_list.serialize_json(
            value["action_configurations"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["displayName"] = value["display_name"]
    if "authentication_detail" in value:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authenticationDetail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.serialize_json(
                value["authentication_detail"]
            )
        )
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataAccessorRequest:
    out: CreateDataAccessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    else:
        raise DeserializationError("CreateDataAccessorRequest.principal required")
    if data.get("actionConfigurations") is not None:
        import capo_qbusiness.types.action_configuration_list

        out["action_configurations"] = (
            capo_qbusiness.types.action_configuration_list.deserialize_json(
                data["actionConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataAccessorRequest.action_configurations required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateDataAccessorRequest.display_name required")
    if data.get("authenticationDetail") is not None:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateDataAccessorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
