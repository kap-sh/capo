"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateSourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.fqdn_for_action_framework
    import capo_mgn.types.operating_system_string
    import capo_mgn.types.source_server_connector_action
    import capo_mgn.types.source_server_id
    import capo_mgn.types.user_provided_id


class UpdateSourceServerRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Update Source Server request account ID.</p>"""
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Update Source Server request source server ID.</p>"""
    connector_action: NotRequired[
        "capo_mgn.types.source_server_connector_action.SourceServerConnectorAction"
    ]
    """<p>Update Source Server request connector action.</p>"""
    user_provided_id: NotRequired["capo_mgn.types.user_provided_id.UserProvidedId"]
    """<p>Update Source Server request user provided ID.</p>"""
    fqdn_for_action_framework: NotRequired[
        "capo_mgn.types.fqdn_for_action_framework.FqdnForActionFramework"
    ]
    """<p>Update Source Server request FQDN for action framework.</p>"""
    platform: NotRequired[
        "capo_mgn.types.operating_system_string.OperatingSystemString"
    ]
    """<p>Update Source Server request platform operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceServerRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    out["sourceServerID"] = value["source_server_id"]
    if "connector_action" in value:
        import capo_mgn.types.source_server_connector_action

        out["connectorAction"] = (
            capo_mgn.types.source_server_connector_action.serialize_json(
                value["connector_action"]
            )
        )
    if "user_provided_id" in value:
        out["userProvidedID"] = value["user_provided_id"]
    if "fqdn_for_action_framework" in value:
        out["fqdnForActionFramework"] = value["fqdn_for_action_framework"]
    if "platform" in value:
        out["platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> UpdateSourceServerRequest:
    out: UpdateSourceServerRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("connectorAction") is not None:
        import capo_mgn.types.source_server_connector_action

        out["connector_action"] = (
            capo_mgn.types.source_server_connector_action.deserialize_json(
                data["connectorAction"]
            )
        )
    if data.get("userProvidedID") is not None:
        out["user_provided_id"] = data["userProvidedID"]
    if data.get("fqdnForActionFramework") is not None:
        out["fqdn_for_action_framework"] = data["fqdnForActionFramework"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    return out
