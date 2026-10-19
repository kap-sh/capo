"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateDataAccessorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_configuration_list
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.data_accessor_authentication_detail
    import capo_qbusiness.types.data_accessor_id
    import capo_qbusiness.types.data_accessor_name


class UpdateDataAccessorRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""
    data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the data accessor to update.</p>"""
    action_configurations: (
        "capo_qbusiness.types.action_configuration_list.ActionConfigurationList"
    )
    """<p>The updated list of action configurations specifying the allowed actions and any associated filters.</p>"""
    authentication_detail: NotRequired[
        "capo_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The updated authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>"""
    display_name: NotRequired[
        "capo_qbusiness.types.data_accessor_name.DataAccessorName"
    ]
    """<p>The updated friendly name for the data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAccessorRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.action_configuration_list

    out["actionConfigurations"] = (
        capo_qbusiness.types.action_configuration_list.serialize_json(
            value["action_configurations"]
        )
    )
    if "authentication_detail" in value:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authenticationDetail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.serialize_json(
                value["authentication_detail"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> UpdateDataAccessorRequest:
    out: UpdateDataAccessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("actionConfigurations") is not None:
        import capo_qbusiness.types.action_configuration_list

        out["action_configurations"] = (
            capo_qbusiness.types.action_configuration_list.deserialize_json(
                data["actionConfigurations"]
            )
        )
    else:
        out["action_configurations"] = []
    if data.get("authenticationDetail") is not None:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    return out


def redact_sensitive(value: UpdateDataAccessorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
