"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentAccessControlEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.access_control_access
    import capo_bedrock_agent.types.access_control_principal_type


class DocumentAccessControlEntry(TypedDict, closed=True):
    name: "str"
    """<p>The user identifier.</p>"""
    type: "capo_bedrock_agent.types.access_control_principal_type.AccessControlPrincipalType"
    """<p>The type of principal.</p>"""
    access: "capo_bedrock_agent.types.access_control_access.AccessControlAccess"
    """<p>Whether to allow or deny access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAccessControlEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent.types.access_control_principal_type

    out["type"] = capo_bedrock_agent.types.access_control_principal_type.serialize_json(
        value["type"]
    )
    import capo_bedrock_agent.types.access_control_access

    out["access"] = capo_bedrock_agent.types.access_control_access.serialize_json(
        value["access"]
    )
    return out


def deserialize_json(data: dict) -> DocumentAccessControlEntry:
    out: DocumentAccessControlEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agent.types.access_control_principal_type

        out["type"] = (
            capo_bedrock_agent.types.access_control_principal_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.access_control_principal_type.AccessControlPrincipalType",
            "",
        )
    if data.get("access") is not None:
        import capo_bedrock_agent.types.access_control_access

        out["access"] = capo_bedrock_agent.types.access_control_access.deserialize_json(
            data["access"]
        )
    else:
        import typing

        out["access"] = typing.cast(
            "capo_bedrock_agent.types.access_control_access.AccessControlAccess", ""
        )
    return out
