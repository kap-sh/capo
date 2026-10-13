"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedInputItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier
    import capo_verifiedpermissions.types.context_definition
    import capo_verifiedpermissions.types.entity_identifier


class BatchIsAuthorizedInputItem(TypedDict, closed=True):
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the principal for which the authorization decision is to be made.</p>"""
    action: NotRequired[
        "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
    ]
    """<p>Specifies the requested action to be authorized. For example, <code>PhotoFlash::ReadPhoto</code>.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the resource that you want an authorization decision for. For example, <code>PhotoFlash::Photo</code>.</p>"""
    context: NotRequired[
        "capo_verifiedpermissions.types.context_definition.ContextDefinition"
    ]
    """<p>Specifies additional context that can be used to make more granular authorization decisions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedInputItem) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "action" in value:
        import capo_verifiedpermissions.types.action_identifier

        out["action"] = (
            capo_verifiedpermissions.types.action_identifier.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "context" in value:
        import capo_verifiedpermissions.types.context_definition

        out["context"] = (
            capo_verifiedpermissions.types.context_definition.serialize_aws_json_1_0(
                value["context"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedInputItem:
    out: BatchIsAuthorizedInputItem = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("action") is not None:
        import capo_verifiedpermissions.types.action_identifier

        out["action"] = (
            capo_verifiedpermissions.types.action_identifier.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    if data.get("resource") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("context") is not None:
        import capo_verifiedpermissions.types.context_definition

        out["context"] = (
            capo_verifiedpermissions.types.context_definition.deserialize_aws_json_1_0(
                data["context"]
            )
        )
    return out


def redact_sensitive(value: BatchIsAuthorizedInputItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["principal"]
            )
        )
    if "action" in value:
        import capo_verifiedpermissions.types.action_identifier

        out["action"] = (
            capo_verifiedpermissions.types.action_identifier.redact_sensitive(
                value["action"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["resource"]
            )
        )
    if "context" in value:
        import capo_verifiedpermissions.types.context_definition

        out["context"] = (
            capo_verifiedpermissions.types.context_definition.redact_sensitive(
                value["context"]
            )
        )
    return out
