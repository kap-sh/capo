"""Generated from Smithy shape ``com.amazonaws.securityagent#CreatePrivateConnectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_mode
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.tag_map


class CreatePrivateConnectionInput(TypedDict, closed=True):
    private_connection_name: (
        "capo_securityagent.types.private_connection_name.PrivateConnectionName"
    )
    """<p>A unique name for the private connection within your account.</p>"""
    mode: "capo_securityagent.types.private_connection_mode.PrivateConnectionMode"
    """<p>The configuration for the private connection. Specify either a service-managed or a self-managed mode.</p>"""
    tags: NotRequired["capo_securityagent.types.tag_map.TagMap"]
    """<p>The tags to attach to the private connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateConnectionInput) -> dict:
    out: dict = {}
    out["privateConnectionName"] = value["private_connection_name"]
    import capo_securityagent.types.private_connection_mode

    out["mode"] = capo_securityagent.types.private_connection_mode.serialize_json(
        value["mode"]
    )
    if "tags" in value:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePrivateConnectionInput:
    out: CreatePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    else:
        out["private_connection_name"] = ""
    if data.get("mode") is not None:
        import capo_securityagent.types.private_connection_mode

        out["mode"] = capo_securityagent.types.private_connection_mode.deserialize_json(
            data["mode"]
        )
    else:
        import capo_securityagent.types._unknown

        out["mode"] = capo_securityagent.types._unknown.UnknownUnionMember("")
    if data.get("tags") is not None:
        import capo_securityagent.types.tag_map

        out["tags"] = capo_securityagent.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreatePrivateConnectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mode" in value:
        import capo_securityagent.types.private_connection_mode

        out["mode"] = capo_securityagent.types.private_connection_mode.redact_sensitive(
            value["mode"]
        )
    return out
