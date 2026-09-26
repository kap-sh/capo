"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateTemplateSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.template_identifier


class CreateTemplateSnapshotInput(TypedDict, closed=True):
    template_identifier: (
        "capo_network_security_manager.types.template_identifier.TemplateIdentifier"
    )
    """<p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the snapshot when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateSnapshotInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateSnapshotInput:
    out: CreateTemplateSnapshotInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
